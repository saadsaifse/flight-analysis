# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AnimalMovementAnalysis - Processing analysis funcionality

 This plugin finds correlation between air temperature and activity patterns of animals
 chosen by the user in the area of North Rhine-Westphalia
                               -------------------
        begin                : 2019-06-23
        copyright            : (C) 2019 by Anna Formaniuk, Violeta Ana Luz Sosa León, Muhammad Saad Saif, Tina Baidar, Aditya Rajendra Kudekar
        email                : vsosaleo@uni-muenster.de
 ***************************************************************************/

"""
import os
from qgis.core import *
import qgis.utils

#Create data object
dataSample = qgis.utils.iface.activeLayer();

features = dataSample.getFeatures()

data={}

for feature in features:
    attributes = feature.attributes()
    data[feature.id()]={}

    for field, attr in zip(dataSample.fields(), attributes):
        data[feature.id()][field.name()]=attr

#calculateCummulativeFDistancePerDay(data)
#calculateSeasonFlight(data)
