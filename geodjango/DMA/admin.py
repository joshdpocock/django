from django.contrib.gis import admin
from .models import area_6_DMAs

admin.site.register(area_6_DMAs, admin.OSMGeoAdmin)

# Register your models here.
