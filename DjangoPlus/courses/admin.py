from django.contrib import admin
from .models import Category, Course, Episode, Comment, ContactUs


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image_thumbnail']


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['__str__']


class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name', 'last_name', 'email', 'message')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Comment)
admin.site.register(ContactUs, ContactUsAdmin)


