from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from courses.models import Course
from .models import ShopCart


@login_required
def add_to_shopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    course = Course.objects.get(id=id)

    if request.method == 'POST':
        data = ShopCart.objects.create(course=course, user_id=current_user.id)
        data.save()
        messages.success(request, 'دوره شما به سبد خرید افزوده شد', 'success')
        return redirect(url)
    

class ShopCartView(LoginRequiredMixin, View):
    template_name = "shopcart.html"
    def get(self, request):
        current_user = request.user
        shopcart = ShopCart.objects.filter(user_id=current_user.id)
        return render(request, self.template_name, {'shopcart':shopcart})


class DeleteShopCart(LoginRequiredMixin, View):
    def get(self, request, id):
        url = request.META.get('HTTP_REFERER')
        ShopCart.objects.filter(id=id).delete()
        messages.success(request, "دوره مورد نظر از سبد خرید حذف شد", "success")
        return redirect(url)