from django.urls import path
from . import views


app_name="courses"
urlpatterns = [
    path('navbar/', views.navbar, name="navbar"),
    path('', views.Home.as_view(), name="home"),
    path('course-detail/<slug:slug>/<int:id>/', views.CourseDetail.as_view(), name="courses-detail"),
    path('add-comment/<int:course_id>/', views.AddComment.as_view(), name='comment'),
    path('add-reply/<int:course_id>/<int:comment_id>', views.AddReply.as_view(), name='reply'),
    path('courses-list/', views.CourseList.as_view(), name="courses-list"),
    path('aboutus/', views.AboutUs.as_view(), name="aboutus"),
    path('contactus/', views.ContactUsView.as_view(), name="contactus"),
]
