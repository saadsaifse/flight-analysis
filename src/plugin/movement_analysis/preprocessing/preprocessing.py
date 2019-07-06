# from qgis.core import QgsVectorDataProvider
from qgis.core import *
from PyQt5.QtCore import *
import qgis.utils
import os
import time
import dateutil.parser
from datetime import datetime as dt

def preprocessing (shape_layer):
    uri2 = "file:///F:/Dokumente/Uni_Msc/2019_SS/PIGIS/project/birds-repo/src/plugin/movement_analysis/preprocessing/data/temperature.csv?delimiter=,"

    start = dt.now()
    print("Script execution started at: ", start)

    # first remove the unnecessary attributes
    caps = shape_layer.dataProvider().capabilities()
    indices = []
    useless_fields = ("start_time", "utm_east", "utm_north", "utm_zone", "battery_vo", "fix_batter", "horizontal", "key_bin_ch", "speed_accu", "status", "temperatur", "type_of_fi", "used_time_", "heading", "outlier_ma", "visible", "sensor_typ","individual", "tag_ident", "speed", "height", "study_name", "date", "time")
    for field in shape_layer.fields():
        for value in useless_fields:
            index = shape_layer.fields().lookupField(value)
            indices.append(index)

    if caps & QgsVectorDataProvider.DeleteAttributes:
        res = shape_layer.dataProvider().deleteAttributes(indices)

    # update to propagate the changes
    shape_layer.updateFields()

    end = dt.now()
    total_time = end - start
    print("Script deleting ran for : ", total_time)

    # create new attributes
    caps = shape_layer.dataProvider().capabilities()
    if caps & QgsVectorDataProvider.AddAttributes:
        res = shape_layer.dataProvider().addAttributes(
            [QgsField("date", QVariant.Date), QgsField("dateString", QVariant.String), QgsField("timeString", QVariant.String)])


    # update to propagate the changes
    shape_layer.updateFields()

    end2 = dt.now()
    total_time = end2 - end
    print("Script creating new attributes ran for : ", total_time)

    # populate the attributes with values
    field_name_i_search = ['date', 'dateString', 'timeString']
    fields = shape_layer.dataProvider().fields()
    indexlist = []
    index = 0
    for field in shape_layer.fields():
        for newfield in field_name_i_search:
            if field.name() == newfield:
                indexlist.append(index)
                break
        index += 1
    updates = {}
    for feat in shape_layer.getFeatures():
        # split date and time values from timestamp field
        date, time = feat['timestamp'].split(" ")
        dateD = dt.strptime(date,'%Y-%m-%d')
        dateS = "{:%d-%B-%Y}".format(dateD)
        updates[feat.id()] = {indexlist[0]: QVariant(QDateTime(dateD)), indexlist[1]: dateS, indexlist[2]: time}

    end3 = dt.now()
    total_time = end3 - end2
    print("Script now ready to update values ", total_time)

    shape_layer.dataProvider().changeAttributeValues(updates)

    end4 = dt.now()
    total_time = end4 - end3
    print("Script new fields populating ran for : ", total_time)

    infoLyr = QgsVectorLayer(uri2, 'temp', 'delimitedtext')
    caps = infoLyr.dataProvider().capabilities()

    # for field in infoLyr.fields():
    #     print(field.name(), field.typeName())

    print("infoLyr valid? ", infoLyr.isValid())
    csvField = 'date'
    shpField = 'dateString'
    joinObject = QgsVectorLayerJoinInfo()
    joinObject.setJoinFieldName(csvField)
    joinObject.setTargetFieldName(shpField)
    joinObject.setJoinLayerId(infoLyr.id())
    joinObject.setUsingMemoryCache(True)
    joinObject.setJoinLayer(infoLyr)
    shape_layer.addJoin(joinObject)

    caps = shape_layer.dataProvider().capabilities()
    if caps & QgsVectorDataProvider.AddAttributes:
        res = shape_layer.dataProvider().addAttributes([QgsField("avg_temp", QVariant.Double)])
    shape_layer.updateFields()

    end5 = dt.now()
    total_time = end5 - end4
    print("Script joining ran for : ", total_time)

    with edit(shape_layer):
        for feature in shape_layer.getFeatures():
            feature.setAttribute(feature.fieldNameIndex("avg_temp"), (feature["temp_tmax"] + feature["temp_tmin"]) / 2)
            shape_layer.updateFeature(feature)
        print("Done")

    end5 = dt.now()
    total_time = end5 - end4
    print("Script time appending ran for : ", total_time)
    print("DONE")

