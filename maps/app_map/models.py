from __future__ import unicode_literals
from django.contrib.gis.db import models

class Cnotozymi(models.Model):
    gid = models.IntegerField(primary_key = True)
    crop=models.CharField(max_length=50)
    s_ga=models.FloatField()
    harvest=models.FloatField()
    hatrv_inga=models.FloatField()
    geom=models.MultiPolygonField()


class Finalelim(models.Model):
    gid = models.IntegerField(primary_key = True)
    id = models.IntegerField()
    gridcode = models.IntegerField()
    area_ha = models.FloatField()
    comment = models.CharField(max_length=50)
    geom = models.MultiPolygonField()


