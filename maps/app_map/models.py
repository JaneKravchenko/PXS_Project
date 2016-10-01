from __future__ import unicode_literals
from django.contrib.gis.db import models

class Cnotozymi(models.Model):
    gid = models.IntegerField(primary_key = True)
    crop=models.CharField(max_length=50)
    s_ga=models.FloatField()
    harvest=models.FloatField()
    hatrv_inga=models.FloatField()
    geom=models.MultiPolygonField()

