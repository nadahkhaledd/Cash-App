from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    number = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    current_credit = models.FloatField(default=0.0)

    def __str__(self):
        return self.number


# class Admin(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=100)


