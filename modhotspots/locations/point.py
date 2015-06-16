from django.db import models

class Point(models.model):
    lon = models.FloatField()
    lat = models.FloatField()

