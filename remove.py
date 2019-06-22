import os
from qgis.core import *
import qgis.utils

# path to shapefile
shape_file = os.path.join("C:\\", "WWU", "Sem1","Python","Project","eagle_owl","points.shp")
# load the shapefile
layer = iface.addVectorLayer(shape_file, "points", "ogr")
caps = Vlayer.dataProvider().capabilities()
print(caps)
indices = []
useless_fields = ("battery_vo", "fix_batter", "horizontal", "key_bin_ch" ,"speed_accu","status", "temperatur", "type_of_fi", "used_time_","heading", "outlier_ma", "visible","sensor_typ", "individual","tag_ident", "ind_ident", "study_name", "date")
print(useless_fields)
for field in layer.fields():
    for value in useless_fields:
        index = layer.fields().lookupField(value)
        indices.append(index)
print(indices)

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = layer.dataProvider().deleteAttributes(indices)

## update to propagate the changes  
layer.updateFields()