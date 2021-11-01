from django.db import models
from account.models import MyUser
from courses.models import TimeStamp, Course



class Order(TimeStamp):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=8, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ip = models.CharField(blank=True, max_length=20)
    status = models.CharField(max_length=15, choices=STATUS, default='New')

    def __str__(self):
        return self.user.username


class OrderCourse(TimeStamp):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'

    @property
    def status_order(self):
        return self.order.status

    @property
    def sell(self):
        return self.course.sell



    