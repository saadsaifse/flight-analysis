import os
from qgis.core import *
import qgis.utils

# path to shapefile
shape_file = os.path.join("C:\\", "WWU", "Sem1","Python","Project","eagle_owl","points.shp")
# load the shapefile
layer = iface.addVectorLayer(shape_file, "points", "ogr")
caps = layer.dataProvider().capabilities()
print(caps)
indices = []
useless_fields = ("start_time", "utm_east", "utm_north", "utm_zone",  "battery_vo", "fix_batter", "horizontal", "key_bin_ch","speed_accu","status", "temperatur", "type_of_fi", "used_time_","heading", "outlier_ma", "visible","sensor_typ", "individual","tag_ident","study_name", "date", "time")
for field in layer.fields():
    for value in useless_fields:
        index = layer.fields().lookupField(value)
        indices.append(index)

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = layer.dataProvider().deleteAttributes(indices)

## update to propagate the changes  
layer.updateFields()