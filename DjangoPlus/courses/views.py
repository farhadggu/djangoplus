from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.models import ShopCart
from order.models import Order, OrderCourse
from .models import Category, Course, Episode, Comment, ContactUs
from .forms import SearchForm, CommentForm, ReplyForm, ContactForm


def navbar(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.course.total_price

    form = SearchForm()

    return render(request, 'shared/navbar.html', {'category':category, 'shopcart':shopcart, 'total':total, 'form':form})


class Home(View):
    template_name = 'home.html'
    def get(self, request):
        categories = Category.objects.all()
        courses = Course.objects.all()
        return render(request, self.template_name, {"categories": categories, "courses": courses})


class CourseDetail(View):
    template_name = "course-detail.html"
    def get(self, request, slug, id):
        course = get_object_or_404(Course, slug=slug, id=id)
        episode = Episode.objects.all()
        comment_form = CommentForm()
        reply_form = ReplyForm()
        comment = Comment.objects.filter(courses_id=id, is_reply=False)
        context = {
            'course': course, 'episode': episode,
            'reply_form' : reply_form, 'comment_form': comment_form,
            'comment': comment
        }
        try:
            order = OrderCourse.objects.get(user_id=request.user.id, course_id=id)
            context1 = {
                'course': course, 'episode': episode,
                'reply_form' : reply_form, 'comment_form': comment_form,
                'comment': comment, 'order': order,
            }
            return render(request, self.template_name, context1)
        except:
            return render(request, self.template_name, context)


class AddComment(LoginRequiredMixin, View):
    def post(self, request, course_id):
        url = request.META.get('HTTP_REFERER')
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                user_id = request.user.id,
                comment = cd['comment'],
                courses_id = course_id
            )
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
        return redirect(url)


class AddReply(LoginRequiredMixin, View):
    def post(self, request, course_id, comment_id):
        url = request.META.get('HTTP_REFERER')
        form = ReplyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                comment = cd['comment'],
                user_id = request.user.id,
                courses_id = course_id,
                reply_id = comment_id,
                is_reply = True,
            )
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
        return redirect(url)


class CourseList(View):
    template_name = 'course-list.html'
    def get(self, request):
        courses = Course.objects.all()

        paginator = Paginator(courses, 2)
        page_number = request.GET.get('page')
        data = request.GET.copy()
        if 'page' in data:
            del data['page']
        page_obj = paginator.get_page(page_number)

        form = SearchForm()
        if 'search' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                info = form.cleaned_data['search']
                page_obj = courses.filter(
                    Q(title__icontains=info) | Q(desc__icontains=info)
                )
                paginator = Paginator(page_obj, 2)
                page_number = request.GET.get('page')
                data = request.GET.copy()
                if 'page' in data:
                    del data['page']
                page_obj = paginator.get_page(page_number)
        return render(request, self.template_name, {'courses': page_obj, 'data':urlencode(data)})


class AboutUs(View):
    template_name = 'aboutus.html'
    def get(self, request):
        return render(request, self.template_name, {})


class ContactUsView(View):
    template_name = 'contactus.html'
    form_class = ContactForm
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactUs.objects.create(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                email = cd['email'],
                message = cd['message'],
            )
            messages.success(request, 'تیکت شما با موفقیت ثبت شد منتظر پاسخی که به ایمیل شما فرستاده میشه باشید', 'success')
            return redirect('courses:contactus')