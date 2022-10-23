from email.policy import default
from enum import unique
from django.db import models

# Create your models here.

class Account(models.Model):
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    join_date = models.DateField()
    is_admin = models.BooleanField(default=False)

