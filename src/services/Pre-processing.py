def preprocessing (shape_layer, csv):

    from qgis.core import *
    import qgis.utils
    import os


    caps = shape_layer.dataProvider().capabilities()
    if caps & QgsVectorDataProvider.AddAttributes:
        res = shape_layer.dataProvider().addAttributes(
            [QgsField("date", QVariant.DateTime), QgsField("time_str", QVariant.String)])

    shape_layer.updateFields()

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
    updates = {}
    for feat in shape_layer.getFeatures():
        # split date and time values from timestamp field
        date_str, time_str = feat['timestamp'].split(" ")

        #convert date format from string to date
        date=datetime.datetime.strptime(date_str, '%Y-%m-%d' ).date()

        # Update the empty field in the shapefile
        updates[feat.id()] = {indexlist[0]: date, indexlist[1]: time_str}
    shape_layer.dataProvider().changeAttributeValues(updates)

    shape_layer.updateFields()

    layer = shape_layer
    caps = layer.dataProvider().capabilities()
    indices = []
    useless_fields = ("start_time", "utm_east", "utm_north", "utm_zone", "battery_vo", "fix_batter", "horizontal", "key_bin_ch", "speed_accu", "status", "temperatur", "type_of_fi", "used_time_", "heading", "outlier_ma", "visible", "sensor_typ","individual", "tag_ident", "study_name", "date", "time")
    for field in layer.fields():
        for value in useless_fields:
            index = layer.fields().lookupField(value)
            indices.append(index)

    if caps & QgsVectorDataProvider.DeleteAttributes:
        res = layer.dataProvider().deleteAttributes(indices)

    ## update to propagate the changes
    layer.updateFields()

    vectorLyr = layer
    uri = csv

    infoLyr = QgsVectorLayer(uri, 'temp', 'delimitedtext')
    csvField = 'date'
    shpField = 'date'
    joinObject = QgsVectorLayerJoinInfo()
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

    with edit(vectorLyr):
        for feature in vectorLyr.getFeatures():
            feature.setAttribute(feature.fieldNameIndex("avg_temp"), (feature["temp_tmax"] + feature["temp_tmin"]) / 2)
            vectorLyr.updateFeature(feature)
        print("Done")

