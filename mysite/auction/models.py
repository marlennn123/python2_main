from django.db import models
from datetime import date


class Car(models.Model):
    category = models.CharField(max_length=32)
    marka = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    with_photo = models.BooleanField(default=False)
    color = models.CharField(max_length=32)
    volume = models.FloatField()
    description = models.TextField()


class Bet(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    number = models.IntegerField()
    total_number = models.IntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()