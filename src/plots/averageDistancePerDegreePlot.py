import os
import sys

modelsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models')
print(modelsPath)
sys.path.append(modelsPath)

import pylab as plt
import numpy as np
from averageDistancePerDegree import AverageDistancePerDegree

def plot():
    model = AverageDistancePerDegree()
    data = model.getDummyData()

    tempratures = []
    distances = []
    for i in data:
        tempratures.append(i.temp)
        distances.append(i.avgDistance)

    plt.style.use('ggplot')
    fig = plt.figure(1)
    ax = plt.gca()
    ax.bar(tempratures, distances , lw = 2)
    # set the axis labels
    ax.set_xlabel(r'$temp$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$avg. distance$', fontsize=14, labelpad=25, rotation=0)
    plt.show()

if __name__ == "__main__":
    plot()

