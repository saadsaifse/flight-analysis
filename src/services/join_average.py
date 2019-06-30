import os
from qgis.core import *
import qgis.utils

vectorLyr = iface.activeLayer() 
uri='file:///C:/WWU/Sem1/Python/Project/temperature.csv?delimiter=,'

infoLyr=QgsVectorLayer(uri,'temp','delimitedtext')
csvField='date'
shpField='date'
joinObject=QgsVectorLayerJoinInfo()
joinObject.setJoinFieldName(csvField)
joinObject.setTargetFieldName(shpField)
joinObject.setJoinLayerId(infoLyr.id())
joinObject.setUsingMemoryCache(True)
joinObject.setJoinLayer(infoLyr)
vectorLyr.addJoin(joinObject)

caps = vectorLyr.dataProvider().capabilities()
if caps & QgsVectorDataProvider.AddAttributes:
    res = vectorLyr.dataProvider().addAttributes([QgsField("avg_temp", QVariant.Double)])
vectorLyr.updateFields()

with edit (vectorLyr):
    for feature in vectorLyr.getFeatures():
        feature.setAttribute(feature.fieldNameIndex("avg_temp"), (feature["temp_tmax"]+feature["temp_tmin"])/2)
        vectorLyr.updateFeature(feature)
    print("average calculated")