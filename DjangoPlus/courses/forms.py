from django import forms
from .models import Comment, ContactUs


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'جستجو'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'افزودن کامنت'})


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'متن شما', 'rows': '1'})


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام',})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'نام خانوادگی',})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ایمیل',})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'متن شما', 'rows': '4'})