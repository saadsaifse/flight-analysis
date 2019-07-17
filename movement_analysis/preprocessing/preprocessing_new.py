from qgis.core import *
from PyQt5.QtCore import *
import qgis.utils
import os
import time
import dateutil.parser
import csv
from datetime import datetime as dt

"""
# Name: calculateSeasonFlight(date)
# Description: calculate the season for a given date according to the month
# @args:
#       date: date in format YYYY-MM-DD
# @return String season Winter, Spring, Summer, Autumn
"""
def calculateSeasonFlight(date):
    month = date.month
    seasons_month = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter",
    }

    return seasons_month.get(month, 0)

"""
# Name: createCSVObject()
# Description: loads the csv file stored in the local folder
#  and reads to an array
# @return array of mean temperatures for each day in NRW
"""
def createCSVObject():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("Current preprocessing directory: " + current_dir)
    uri = current_dir + "/data/temperature.csv"

    temperatures = []
    with open(uri, mode='r') as infile:
        reader = csv.DictReader(infile)
        for line in reader:
            temperatures.append(line)

    return temperatures

"""
# Name: preprocessing(birds_obj)
# Description: deletes the pre-defined unnecessary attributes
# and creates new ones required in the processing
# @args:
#       birds_obj: the objects of all points, created in the
#           previous step
# @return same objects, but ready for processing
"""
def preprocessing(birds_obj):
    start = dt.now()
    print("Script preprocessing execution started at: ", start)

    # get the temperatures first
    temperatures = createCSVObject()

    end1 = dt.now()
    total_time = end1 - start
    print("Created the temperatures array : ", total_time)

    # define unnecessary attributes
    useless_fields = ["start_time", "utm_east", "utm_north", "utm_zone",
                      "battery_vo", "fix_batter", "horizontal", "key_bin_ch",
                      "speed_accu", "status", "temperatur", "type_of_fi",
                      "used_time_", "heading", "outlier_ma", "visible",
                      "sensor_typ", "individual", "tag_ident", "speed",
                      "height", "study_name", "date", "time"]

    # remove the unnecessary attributes (does it only if it exists)
    for point in birds_obj.values():
        for useless in useless_fields:
            point.pop(useless, None)
        date, time = point["timestamp"].split(" ")
        dateD = dt.strptime(date, '%Y-%m-%d')
        # date as a datetime object, needed distance calculations
        point["date"] = dateD
        # date as a string, needed to append temperatures
        point["dateString"] = "{:%d-%b-%Y}".format(dateD)
        # point["timeString"] = time
        # season required for filtering
        point["season"] = calculateSeasonFlight(dateD)
        # month required for monthly distance analysis
        point["month"] = dateD.month
        # append the temperature of the day to each point as an int
        for row in temperatures:
            if (row["date"] == point["dateString"]):
                point["temp"] = round(float(row["tmin"]))

    end2 = dt.now()
    total_time = end2 - end1
    print("Script removing, adding and joining ran for : ", total_time)

    return birds_obj
