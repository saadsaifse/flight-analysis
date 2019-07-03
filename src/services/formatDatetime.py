#Script to extract date and time store in new fields

import os
from qgis.core import *
import qgis.utils

# path to shapefile
shape_file = r'C:\Users\Tina Baidar\Documents\Geotech\IFGI_2nd_Sem\Python\project\June6\shapefiles\clip_point.shp'

# load the shapefile
shape_layer = iface.addVectorLayer(shape_file, "shape:", "ogr")
if not shape_layer:
    print("Shapefile failed to load!")
else: print("Shapefile loaded!")  


#Add date and time field (string field)
caps = shape_layer.dataProvider().capabilities()
if caps & QgsVectorDataProvider.AddAttributes:
    res = shape_layer.dataProvider().addAttributes(
        [QgsField("date",  QVariant.DateTime),QgsField("time_str",  QVariant.String)])

# Update to propagate the changes  
shape_layer.updateFields()

# Get the index of the newly added fields
field_name_i_search = ['date', 'time_str']
fields = shape_layer.dataProvider().fields()
indexlist = []
index = 0
for field in shape_layer.fields():
    for newfield in field_name_i_search:
        if field.name() == newfield:
            indexlist.append(index)
            break
    index += 1
#print(indexlist)
        


# Initiate a variable to hold the attribute values
updates = {}
for feat in shape_layer.getFeatures():
    # split date and time values from timestamp field
    date_str, time_str = feat['timestamp'].split(" ")

    #convert date format from string to date
    date=datetime.datetime.strptime(date_str, '%Y-%m-%d' ).date()
    
    # Update the empty field in the shapefile
    updates[feat.id()] = {indexlist[0]: date, indexlist[1]: time_str}
#print(updates)

# Use the created dictionary to update the field for all features
shape_layer.dataProvider().changeAttributeValues(updates)

#Update to propagate the changes  
shape_layer.updateFields()

QgsProject.instance().removeMapLayer(shape_layer.id())

print("Done!")
