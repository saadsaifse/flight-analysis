import os
import sys

modelsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models')
print(modelsPath)
sys.path.append(modelsPath)

import pylab as plt
from averageDistancePerDegree import AverageDistancePerDegree

def plot(birdId, temperatures, averageDistances):
    """Plots average distances against temperatures

    Parameters:
        birdId (str): The ID of the bird
        temperatures (list): List of temperature values
        averageDistances (list): List of average distances
    """    

    plt.style.use('ggplot')
    fig = plt.figure(1)
    ax = plt.gca()
    ax.bar(temperatures, averageDistances , lw = 1)
    # set the axis labels
    ax.set_xlabel(r'$temperature$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$avg. distance$', fontsize=14, labelpad=10, rotation=90)

    # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)
    # add a legend
    leg = plt.legend( [birdId], loc=1 )
    fr = leg.get_frame()
    fr.set_facecolor('w')
    fr.set_alpha(.7)

    plt.title('Average distances')
    plt.show()

if __name__ == "__main__":
    model = AverageDistancePerDegree()
    data = model.getDummyData()

    temperatures = []
    distances = []
    for i in data:
        temperatures.append(i.temp)
        distances.append(i.avgDistance)

    plot(data[0].birdId, temperatures, distances)

