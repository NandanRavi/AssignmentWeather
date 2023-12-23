# weather_app/models.py
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return self.city
