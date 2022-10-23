from email.policy import default
from django.db import models

# Create your models here.

class Cell(models.Model):
    subject = models.CharField(max_length=20)
    cabinet_number = models.CharField(max_length=10)
    group_name = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=20)

class Week(models.Model):
    is_odd = models.BooleanField(default=True)