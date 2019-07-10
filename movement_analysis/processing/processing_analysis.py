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
import collections
from datetime import datetime as dt, timedelta

# Name: constructDataObject(dataSample)
# Description: Create data object to arrange fields for processing from active shapefile
#@args:
#       dataSample: layer
# @return dictionary data

def constructDataObject(dataSample):
    data={}

    # dataSample = qgis.utils.iface.activeLayer();
    features = dataSample.getFeatures()

    for feature in features:
        attributes = feature.attributes()
        data[feature.id()]={}

        for field, attr in zip(dataSample.fields(), attributes):
            data[feature.id()][field.name()]=attr

            # if field.name()=="date":
            #     data[feature.id()]["season"]=calculateSeasonFlight(attr)

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

    distance=distanceF.measureLine(point1, point2)

    return distance

# Name: calculateSeasonFlight(date)
# Description: calculate the season for a given date according to the month
# @args:
#       date: date in format YYYY-MM-DD
# @return String season Winter, Spring, Summer, Autumn
def calculateSeasonFlight(date):
    month=date.month
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

    return seasons_month.get(month, 0)




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
        grouped[data[outer_k]["ind_ident"]]=data

    for bird_id, bird_data in grouped.items():
        i=0

        for feature,dayData in bird_data.items():
            if feature+1 in list(bird_data.keys()) and dayData['ind_ident']==bird_id:
                date=datetime.strptime(dayData['timestamp'], '%Y-%m-%d %H:%M:%S')

                date_later=datetime.strptime(bird_data[feature+1]['timestamp'], '%Y-%m-%d %H:%M:%S')
                current_date=dayData['date']

                #Create start of the day
                date_start=current_date+timedelta(hours=17)
                #Create the end of the day
                date_end=current_date+timedelta(days=1, hours=5)
                #print ("This bird wake ups at",date_start," and goes to bed at ",date_end)

                distance=calculateDistancePoints(bird_data[feature]['long'],bird_data[feature]['lat'],bird_data[feature+1]['long'],bird_data[feature+1]['lat'])

                if date>date_start and date<date_end and date_later>date_start and date_later<date_end:
                    birdInd[bird_id][i]={'date':current_date.strftime('%Y-%m-%d'),'distance':distance,'temp':bird_data[feature]['temp'],'season':bird_data[feature]['season'],'month':bird_data[feature]['month']}
                else:
                    birdInd[bird_id][i]={'date':(current_date+timedelta(days=-1)).strftime('%Y-%m-%d'),'distance':distance,'temp':bird_data[feature]['avg_temp'],'season':bird_data[feature]['season'],'month':bird_data[feature]['month']}

                i+=1

    return birdInd

def processBird(data):
    total_distance=0
    birdDayResults=collections.defaultdict(dict)
    k=0

    for key,distanceData in data.items():
        for i, values in distanceData.items():
            if i+1 in list(distanceData.keys()) and distanceData[i]["date"]==distanceData[i+1]["date"]:
                total_distance=total_distance+values["distance"]
            else:
                birdDayResults[k]={'bird_id':key,'date':distanceData[i-1]["date"],'distance':round(total_distance),'temp':distanceData[i-1]["temp"],'season':distanceData[i-1]["season"], 'month':distanceData[i-1]["month"]}
                total_distance=0
                k+=1

    return birdDayResults

def monthlyDistanceTemp(distanceData):
    monthlyDistanceTemp=collections.defaultdict(list)
    avg_temp=createEmptyList()
    avg_dist=createEmptyList()
    total_distance=0
    total_temperature=0

    monthList=createMonthList()
    k=1

    for i, values in distanceData.items():
        if i+1 in list(distanceData.keys()) and distanceData[i]["month"]==distanceData[i+1]["month"]:
            total_distance=total_distance+values["distance"]
            total_temperature=total_temperature+values["temp"]
            k+=1
        else:
            avg_temp[distanceData[i]["month"]-1]=round(total_distance/k)
            avg_dist[distanceData[i]["month"]-1]=round(total_temperature/k)

            total_distance=0
            total_temperature=0
            k=1

    monthlyDistanceTemp=[monthList,avg_temp,avg_dist]

    return monthlyDistanceTemp

def createMonthList():
    monthList=[]
    monthList=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    return monthList

def createEmptyList():
    emptyList=[0,0,0,0,0,0,0,0,0,0,0,0]

    return emptyList

def distancePerTemp(distanceData):
    temp=collections.defaultdict(list)

    i=0

    for i, values in distanceData.items():

        if i+1 in list(distanceData.keys()) and distanceData[i]["temp"]==distanceData[i+1]["temp"]:
            temp[values["temp"]].append(values["distance"])
        else:
            temp[values["temp"]].append(values["distance"])

    total=[]
    second=[]

    for i, values in temp.items():
        second.append(values)

    total=[list(temp.keys()),second]

    return total

def tempAndDist(distanceData):
    temp=[]
    dist=[]
    merge=[]

    for key, values in distanceData.items():
        temp.append(values["temp"])
        dist.append(values["distance"])

    merge=[[temp],[dist]]

    return merge
