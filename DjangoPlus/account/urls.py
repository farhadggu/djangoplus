from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/<int:id>/', views.Profile.as_view(), name="profile"),
    path('change-password/<int:user_id>/', views.ChangePassword.as_view(), name="change-password"),
    path('reset-password', views.ResetPassword.as_view(), name="reset-password"),    
    path('done-password', views.DonePassword.as_view(), name="done-password"),
    path('confirm-password/<uidb64>/<token>/', views.ConfirmPassword.as_view(), name='confirm'),
    path('complete-reset-password/', views.CompeletePassword.as_view(), name='complete'),
]
