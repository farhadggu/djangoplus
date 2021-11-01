from django.db import models
from account.models import MyUser
from courses.models import TimeStamp, Course



class ShopCart(TimeStamp):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'

    @property
    def price(self):
        self.course.total_price