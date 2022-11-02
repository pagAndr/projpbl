from django.db import models

# Create your models here.

class Pair(models.Model):
    subject = models.CharField(max_length=100)
    cabinet = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    odd_week = models.BooleanField(default=True)


"""
class Week(models.Model):
    pair_nr = models.IntegerField()
    day1 = Pair
    day2 = Pair
    day3 = Pair
    day4 = Pair
    day5 = Pair
    day6 = Pair
    day7 = Pair
"""
