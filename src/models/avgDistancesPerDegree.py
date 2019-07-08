import random

class AvgDistancesPerDegree:
    def __init__(self, avgDistances = None, temp = None):
        self.avgDistances = avgDistances
        self.temp = temp

    def getDummyData(self):        
        dummyData = [AvgDistancesPerDegree([ i + 1 for i in range(random.randrange(5, 100)) ], random.randrange(-10, 30)) for i in range(1, 50)]
        return dummyData