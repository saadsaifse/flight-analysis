import random

class AverageDistancePerDegree:
    def __init__(self, birdId = 0, avgDistance = 0, temp = 0):
        self.birdId = birdId
        self.avgDistance = avgDistance
        self.temp = temp

    def getDummyData(self):
        birdIds = ['DEW A0798', 'DEW A1805', 'DEW A1806', 'DEW A1807', 'DEW A0452', 'DEW A1809']     
        dummyData = [AverageDistancePerDegree(random.choice(birdIds), random.randrange(5, 50), random.randrange(-50, 50)) for i in range(1, 100)]
        return dummyData