from django.contrib import admin
from .models import Order, OrderCourse


class OrderCourseInline(admin.TabularInline):
    model = OrderCourse
    readonly_fields = ('user', 'course')
    can_delete = False
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name',]
    readonly_fields = ('__str__', 'first_name', 'last_name', 'code', 'ip')
    can_delete = False
    inlines = [OrderCourseInline]


class OrderCourseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderCourse, OrderCourseAdmin)
