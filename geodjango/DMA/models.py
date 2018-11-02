from django.contrib.gis.db import models
from django.contrib.gis.db import models as geomodels


import random

def random_int():
    return random.randint(5,100)


class area_6_DMAs(models.Model):
    field_1 = models.CharField(max_length=254)
    field_2 = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)
    leakage = models.IntegerField(default = random_int)

    def __str__(self):
        return self.field_2


# Auto-generated `LayerMapping` dictionary for area_6_DMAs model
area_6_dmas_mapping = {
    'field_1': 'field_1',
    'field_2': 'field_2',
    'geom': 'MULTIPOLYGON',
    'leakage': 'leakage'
}

class area_6_bursts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=20)
    geom = models.PointField()

    def __str__(self):
       return str(self.id)

# Auto-generated `LayerMapping` dictionary for area_6_bursts model
area_6_bursts_mapping = {
    'id': 'id',
    'type': 'Type',
    'geom': 'POINT',
}


    
