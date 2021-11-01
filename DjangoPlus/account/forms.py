from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser, Profile


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'first_name', 'last_name', 'is_active', 'is_admin')



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"ایمیل کاربری"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"رمز عبور"}))


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"ایمیل کاربری"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"نام کاربری"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"رمز عبور"}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"تایید رمز عبور"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = MyUser.objects.filter(email=email).exists()
        if qs:
            raise ValidationError('این ایمیل توسط شخص دیگری ثبت شده است')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        qs = MyUser.objects.filter(username=username).exists()
        if qs:
            raise ValidationError('این نام کاربری توسط شخص دیگری ثبت شده است')
        return username

    def clean_re_password(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']

        if password and re_password and password != re_password:
            raise ValidationError('رمز عبور و تایید رمز عبور همسان نیستند!')
        return re_password



class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'first_name', 'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام خانوادگی'})