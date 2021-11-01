from django.urls import path
from . import views


app_name="cart"
urlpatterns = [
    path('add-to-shopcart/<int:id>', views.add_to_shopcart, name="addtoshapcart"),
    path('', views.ShopCartView.as_view(), name='shop-cart'),
    path('deleteshopcart/<int:id>', views.DeleteShopCart.as_view(), name='delete-shop-cart'),

]
