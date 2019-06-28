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

# Name: constructObject()
# Description: Create data object to arrange fields for processing from active shapefile
# @return dictionary data

def constructObject():
    data={}

    dataSample = qgis.utils.iface.activeLayer();
    features = dataSample.getFeatures()

    for feature in features:
        attributes = feature.attributes()
        data[feature.id()]={}

        for field, attr in zip(dataSample.fields(), attributes):
            data[feature.id()][field.name()]=attr

    return data

# Name: calculateDistancePoints(xa,ya,xb,yb)
# Description: Measure linear distance between two points in WGS84 Ellipsoid
# @args:
#       xa: longitute pointA
#       ya: latitude pointA
#       xb: longitute pointB
#       yb: latitude pointB
# @return float distance in meters

def calculateDistancePoints(xa,ya,xb,yb):
    distance=0

    distanceF = QgsDistanceArea()
    distanceF.setEllipsoid('WGS84')

    point1=QgsPointXY(xa, ya)
    point2=QgsPointXY(xb,yb)

    distance=d.measureLine(point1, point2)

    return distance

#calculateCummulativeFDistancePerDay(data)

# Name: calculateSeasonFlight(date)
# Description: calculate the season for a given date according to the month
# @args:
#       date: date in format YYYY-MM-DD
# @return String season Winter, Spring, Summer, Autumn
def calculateSeasonFlight(date):
    year,month,date=date.split('-')

    seasons_month={
        1:"Winter",
        2:"Winter",
        3:"Spring",
        4:"Spring",
        5:"Spring",
        6:"Summer",
        7:"Summer",
        8:"Summer",
        9:"Autumn",
        10:"Autumn",
        11:"Autumn",
        12:"Winter",
    }

    return seasons_month.get(int(month), "Invalid month value")
