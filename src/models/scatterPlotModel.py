import random

class BirdPoint:
    def __init__(self, birdId = None, lat = None, lon = None, temp = None):
        self.birdId = birdId
        self.lat = lat
        self.lon = lon
        self.temp = temp
    

class ScatterPlotModel:
    def __init__(self, birdId = None, latitudes = None, longitudes = None, temperatures = None):
        self.birdId = birdId
        self.latitudes = latitudes
        self.longitudes = longitudes
        self.temperatures = temperatures

    def getDummyDataSingleBird(self):
        dummyData = ScatterPlotModel('DEW A0798', 
        [ random.uniform(51.96000, 51.96300) for i in range(1, 100) ],
        [ random.uniform(7.62500, 7.62600) for i in range(1, 100) ],
        [ random.randrange(-10, 30) for i in range(1, 100) ])        
        return dummyData