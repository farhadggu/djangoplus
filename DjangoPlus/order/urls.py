from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('', views.order_course, name="order-course"),
    path('request/<total>/', views.send_request, name='payment'),
	path('verify/', views.verify, name='verify'),
]
