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

# Name: constructDataObject()
# Description: Create data object to arrange fields for processing from active shapefile
# @return dictionary data

def constructDataObject():
    data={}

    dataSample = qgis.utils.iface.activeLayer();
    features = dataSample.getFeatures()

    for feature in features:
        attributes = feature.attributes()
        data[feature.id()]={}

        for field, attr in zip(dataSample.fields(), attributes):
            data[feature.id()][field.name()]=attr

            if field.name()=="date":
                data[feature.id()]["season"]=calculateSeasonFlight(attr)

    return data

#Filtering function ()

# Name: filterDataByBird()
# Description: Create data object subset by one bird selected by user
# @return dictionary data filtered per bird selected

def filterDataByBird(data,birds_filter=None):
    data_filtered={}

    if birds_filter is None:
        data_filtered=data
    else:
        data_filtered = {outer_k: data[outer_k] for outer_k in data if data[outer_k]["ind_ident"]==birds_filter}

    return data_filtered

# Name: filterDataByDate()
# Description: Create data object subset by user filters date range init and end
# @return dictionary data filtered between two given dates

def filterDataByDate(data, date_init=None, date_end=None):
    data_filtered={}

    if date_init is None or date_end is None:
        data_filtered=data
    else:
        date_init=datetime.strptime(date_init, '%Y-%m-%d %H:%M:%S')
        date_end=datetime.strptime(date_end, '%Y-%m-%d  %H:%M:%S')

        data_filtered = {outer_k: data[outer_k] for outer_k in data if datetime.strptime(data[outer_k]["timestamp"],'%Y-%m-%d %H:%M:%S')>=date_init and datetime.strptime(data[outer_k]["timestamp"],'%Y-%m-%d %H:%M:%S')<=date_end}

    return data_filtered

# Name: filterDataBySeason()
# Description: Create data object subset by user filters season list
# @return dictionary data filtered between given season(s)

def filterDataBySeason(data,season=["Winter", "Spring", "Summer", "Autumn"]):
    data_filtered={}

    data_filtered = {outer_k: data[outer_k] for outer_k in data if data[outer_k]["season"] in season}

    return data_filtered

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

# Name: calculateSeasonFlight(date)
# Description: calculate the season for a given date according to the month
# @args:
#       date: date in format YYYY-MM-DD
# @return String season Winter, Spring, Summer, Autumn
def calculateSeasonFlight(date):
    month=date.month()
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

    return seasons_month.get(int(month), 0)




# Name: calculateDistancePerDay(data)
# Description: calculate the total distance
# @args:
#       date: dictionary data obvject with features filtered
# @return:
#       Dictionary object id_bird, date, distance, temperature

def calculateDistancePerDay(data):
grouped = collections.defaultdict(dict)
    birdInd=collections.defaultdict(dict)
    #group by bird id
    for outer_k in data:
        #data=processBird(data[outer_k])
        grouped[data[outer_k]["ind_ident"]]=data

    for bird_id, bird_data in grouped.items():

        for feature,dayData in bird_data.items():
            if feature < list(bird_data.keys())[-1]:
                date=datetime.strptime(dayData['timestamp'], '%Y-%m-%d %H:%M:%S')

                date_later=datetime.strptime(bird_data[feature+1]['timestamp'], '%Y-%m-%d %H:%M:%S')
                current_date=datetime.strptime(dayData['date'].toString("yyyy-MM-dd"),'%Y-%m-%d')

                #Create start of the day
                date_start=current_date+timedelta(hours=17)
                #Create the end of the day
                date_end=current_date+timedelta(days=1, hours=5)
                #print ("This bird wake ups at",date_start," and goes to bed at ",date_end)

                #pajaro, dia, distancia, temperatura
                temp= bird_data[feature]['avg_temp']+bird_data[feature+1]['avg_temp']
                distance=calculateDistancePoints(bird_data[feature]['long'],bird_data[feature]['lat'],bird_data[feature+1]['long'],bird_data[feature+1]['lat'])

                if date>date_start and date<date_end and date_later>date_start and date_later<date_end:
                    birdInd[bird_id]={'date':current_date.strftime('%Y-%m-%d'),'time':dayData['timestamp'],'distance':distance,'temp':temp}
                else:
                    birdInd[bird_id]={'date':(current_date+timedelta(days=-1)).strftime('%Y-%m-%d'),'time':dayData['timestamp'],'distance':distance,'temp':temp}

                print (birdInd)

                print("\n\n")

    return True

#Functionality implementation example:


date_init="2011-01-05 00:00:00"
date_end="2011-06-10 23:00:00"
bird="Eagle Owl eobs 1750 / DEW A0322"
data=constructDataObject()
#print(data)
#filteredData_bird=filterDataByBird(data,bird)
fDate=filterDataByDate(data,date_init,date_end)
fSeason=filterDataBySeason(fDate,"Spring")


#print (data[1049])
#print("Filtered by bird\n")
#print(filteredData_bird)
print("Filtered by dates\n")
#print(fSeason)
calculos=calculateDistancePerDay(fSeason)
print(calculos)
