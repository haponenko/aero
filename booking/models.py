from datetime import date
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name


class Booking(models.Model):
    class Meta():
        db_table = 'booking'

    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField(default="")
    date_out = models.DateField(default=date.today)
    date_in = models.DateField(default=date.today)
    country_out = models.CharField(default="", max_length=30)
    country_in = models.CharField(default="", max_length=30)
    state_out = models.CharField(default="", max_length=30)
    state_in = models.CharField(default="", max_length=30)
    city_out = models.CharField(default="", max_length=30)
    city_in = models.CharField(default="", max_length=30)

