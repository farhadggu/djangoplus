from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from suds.client import Client
from django.http.response import HttpResponse
from django.contrib import messages
from cart.models import ShopCart
from account.forms import ProfileForm
from .models import Order, OrderCourse
from .zarinpal import ZarinPal
from courses.models import Course
from DjangoPlus.settings import MERCHANT_ID


@login_required
def order_course(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0

    for rs in shopcart:
        total += rs.course.total_price

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = Order()
            data.user_id = current_user.id
            data.first_name = cd['first_name']
            data.last_name = cd['last_name']
            data.ip = request.META.get('REMOTE_ADDR')
            order_code = get_random_string(8).upper()
            data.code = order_code
            data.save()

            for rs in shopcart:
                detail = OrderCourse()
                detail.order_id = data.id
                detail.course_id = rs.course_id
                detail.user_id = current_user.id
                detail.price = rs.course.total_price
                detail.save()
            request.session['code'] = data.code
            request.session['ordered_id'] = data.id
            return redirect("order:payment", total)
        else:
            messages.error(request, 'لطفا فیلد ها را تکمیل کنید', 'danger')
            return redirect("order:order-course", total)
    else:

        form = ProfileForm()
        context = {
            'shopcart': shopcart,
            'form': form,
            'total': total
        }
        return render(request, 'order_form.html', context)


pay = ZarinPal(merchant=MERCHANT_ID , call_back_url="http://127.0.0.1:8000/order/verify/")


@login_required
def send_request(request, total):
    # email and mobile is optimal
    response = pay.send_request(amount=total, description='توضیحات مربوط به پرداخت', email="Example@test.com",
                               mobile='09123456789')
    if response.get('error_code') is None:
        # redirect object
        return response
    else:
        return HttpResponse(f'Error code: {response.get("error_code")}, Error Message: {response.get("message")}')


def verify(request):
    ordered_id = request.session.get('ordered_id')
    code = request.session.get('code')
    response = pay.verify(request=request, amount='1000')
    current_user = request.user

    if response.get("transaction"):
        if response.get("pay"):
            data = OrderCourse.objects.get(order_id=ordered_id, user_id=request.user.id)
            data.status = 'Completed'           
            data.save()
            course = Course.objects.get(id=1)
            course.sell += 1
            course.save()
            ShopCart.objects.get(user_id=current_user.id).delete()
            messages.success(request, 'تراکنش با موفقت انجام شد', 'success')
            return render(request, 'order_completed.html', {'code':code})
        else:
            data = OrderCourse.objects.get(order_id=ordered_id, user_id=request.user.id)
            data.status = 'Completed'
            data.save()
            course = Course.objects.get(id=1)
            course.sell += 1
            course.save()
            ShopCart.objects.get(user_id=current_user.id).delete()
            messages.success(request, 'تراکنش با موفقت انجام شد', 'success')
            return render(request, 'order_completed.html', {'code':code})
    else:
        if response.get("status") == "ok":
            data = OrderCourse.objects.get(order_id=ordered_id, user_id=request.user.id)
            data.status = 'Completed'
            data.save()
            return HttpResponse(f'Error code: {response.get("error_code")}, Error Message: {response.get("message")}')
        elif response.get("status") == "cancel":
            data = OrderCourse.objects.get(order_id=ordered_id, user_id=request.user.id)
            data.status = 'Canceled'
            data.save()
            messages.error(request, 'تراکنش ناموفق یا به دستور کاربر لغو شده است', 'danger')
            return redirect("order:order-course")