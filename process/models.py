from django.db import models

class Weather(models.Model):
    Date = models.DateField(primary_key=True)
    Time = models.TimeField()
    TemperatureInside = models.FloatField()
    TemperatureOutside = models.FloatField()
    Humidity = models.FloatField()
    RainRate = models.FloatField()
    UVIndex = models.FloatField()
    WindSpeed = models.FloatField()
    Barometer = models.FloatField()

class AverageWeather(models.Model):
    Date = models.DateField(primary_key=True)
    AvgTemperatureInside = models.FloatField()
    AvgTemperatureOutside = models.FloatField()
    AvgHumidity = models.FloatField()
    AvgRainRate = models.FloatField()
    AvgWindSpeed = models.FloatField()
