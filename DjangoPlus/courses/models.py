from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import MyUser
from extensions.utils import jalali_converter


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def jcreated(self):
        return jalali_converter(self.created)

    def jupdated(self):
        return jalali_converter(self.updated)


class Category(TimeStamp):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    class Meta(TimeStamp.Meta):
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:courses-list", args=[self.slug, self.id])
    

class Course(TimeStamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    sell = models.IntegerField()

    class Meta(TimeStamp.Meta):
        ordering = ['-created']
    
    def __str__(self):
        return self.title

    @property
    def get_total_price(self):
        if not self.discount:
            return self.price
        elif self.discount:
            total = (self.price * self.discount) / 100
            return int(self.price - total)
        return self.total_price
    
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price
        super().save(*args, **kwargs)

    def image_thumbnail(self):
        return format_html('<img src="{}" width=100 />'.format(self.image.url))
    image_thumbnail.short_description = 'Image'

    def get_absolute_url(self):
        return reverse("courses:courses-detail", args=[self.slug, self.id])


class Episode(TimeStamp):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    time = models.CharField(max_length=5, null=True, blank=True)
    free = models.BooleanField(default=False)

    class Meta(TimeStamp.Meta):
        ordering = ['created']
    
    def __str__(self):
        return self.title



class Comment(TimeStamp):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    is_reply = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user.username} - {self.comment[:17]}'

    def children(self):
        return Comment.objects.filter(reply=self)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
    