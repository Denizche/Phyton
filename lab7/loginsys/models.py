# Create your models here.

from django.db import models
from datetime import datetime


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    birth_date = models.DateField(default=datetime.now())
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Test(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name