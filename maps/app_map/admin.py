from django.contrib.gis import admin
from .models import WorldBorderl


admin.site.register(WorldBorderl, admin.OSMGeoAdmin)
