from django.contrib import admin
from .models import ShopCart

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(ShopCart, ShopCartAdmin)
