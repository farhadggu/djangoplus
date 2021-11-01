from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views as auth_views
from .forms import LoginForm, ProfileForm, RegisterForm
from .models import MyUser
from .mixins import UserAccessMixin
from order.models import OrderCourse, Order



class LoginView(View):
    template_name = "account/login.html"
    form_class = LoginForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'َشما وارد شدید', 'success')
                return redirect("courses:home")
            else:
                messages.error(request, 'اطلاعات شما نادرست میباشد', 'danger')
                return redirect("account:login")



class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'شما با موفقیت خارج شدید', 'success')
        return redirect("account:login")



class RegisterView(View):
    template_name = "account/register.html"
    form_class = RegisterForm
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = MyUser.objects.create_user(email=cd['email'], username=cd['username'], password=cd['password'])
            user.save()
            messages.success(request, 'حساب شما با موفقیت ایجاد شد', 'success')
            return redirect("account:login")
        else:
            messages.error(request, 'خطا ها رو رفع کنید', 'danger')
            return render(request, self.template_name, {'form':form})


    #template_name = "account/profile.html"
    #form_class = ProfileForm
    #success_url = reverse_lazy("account:profile")
    #queryset = OrderCourse.objects.all()

    #def get_object(self):
        #return MyUser.objects.get(pk=self.request.user.pk)
class Profile(LoginRequiredMixin, UserAccessMixin, View):
    template_name = 'account/profile.html'
    form_class = ProfileForm
    def get(self, request, id):
        user = get_object_or_404(MyUser, id=id)
        form = self.form_class(instance=user)
        order = OrderCourse.objects.filter(user_id=id ,status="Completed")
        return render(request, self.template_name, {'form':form, 'user':user, 'order':order})
    def post(self, request, id):
        user = get_object_or_404(MyUser, id=id)
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل شما ویرایش شد', 'success')
            return redirect("account:profile", request.user.id)




class ChangePassword(LoginRequiredMixin, UserAccessMixin, View):
    template_name = "account/change_password.html"
    form_class = PasswordChangeForm

    def get(self, request, user_id):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form':form})

    def post(self, request, user_id):
        url = request.META.get('HTTP_REFERER')
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'رمز عبور با موفقیت تغییر یافت دوباره وارد شوید', 'success')
            return redirect("account:login")
        messages.error(request, 'خطا', 'danger')
        return render(request, self.template_name, {'form':form})


class ResetPassword(auth_views.PasswordResetView):
    template_name = 'account/reset.html'
    email_template_name = 'account/link.html'
    success_url = reverse_lazy('account:done-password')

    def get_object(self, user_id):
        return MyUser.objects.get(id=user_id)


class DonePassword(auth_views.PasswordResetDoneView):
    template_name = 'account/done.html'

    def get_object(self, user_id):
        return MyUser.objects.get(id=user_id)


class ConfirmPassword(auth_views.PasswordResetConfirmView):
    template_name = 'account/confirm.html'
    success_url = reverse_lazy('account:complete')

    def get_object(self, user_id):
        return MyUser.objects.get(id=user_id)


class CompeletePassword(auth_views.PasswordResetCompleteView):
    template_name = 'account/complete.html'

    def get_object(self, user_id):
        return MyUser.objects.get(id=user_id)
