import os
from django.contrib.gis.utils import LayerMapping
from .models import area_6_DMAs, area_6_bursts

### loads DMAS
#area_6_dmas_mapping = {
    #'field_1': 'field_1',
    #'field_2': 'field_2',
   # 'geom': 'MULTIPOLYGON',
#}

#dmas_shp = world_shp = os.path.abspath(
    #os.path.join(os.path.dirname(__file__), 'data', 'area_6_DMAs.shp'),
#)

#def run(verbose = True):
    #lm = LayerMapping(area_6_DMAs, dmas_shp, area_6_dmas_mapping, transform = False)
    #lm.save(strict=True, verbose = verbose)

##' load area_6_bursts
area_6_bursts_mapping = {
    'id': 'id',
    'type': 'Type',
    'geom': 'POINT',
}

dmas_shp = world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Area_6_bursts.shp'),
)

def run(verbose = True):
    lm = LayerMapping(area_6_bursts, dmas_shp, area_6_bursts_mapping, transform = False)
    lm.save(strict=True, verbose = verbose)





