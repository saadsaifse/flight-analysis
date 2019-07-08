import os
import sys

modelsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models')
print(modelsPath)
sys.path.append(modelsPath)

import matplotlib.pyplot as plt
from avgDistancesPerDegree import AvgDistancesPerDegree

def boxPlot(temperatures, aggregateAverageDistances):
    """Box plots aggregated average distances of all birds, against temperatures

    Parameters:        
        temperatures (list): List of temperature values
        aggregateAverageDistances (list of list): List of lists of aggregate average distances of all birds at temperatures
    """  
    # Showing multiple boxplots on the same window
    plt.style.use('ggplot')
    ax = plt.gca()
    ax.boxplot(aggregateAverageDistances, labels=temperatures)

    # set the axis labels
    ax.set_xlabel(r'$temperature$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$aggregate. distances$', fontsize=14, labelpad=10, rotation=90)

     # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)
    
    plt.title("Birds' aggregate average distances comparison")
    plt.show()


if __name__ == "__main__":
    model = AvgDistancesPerDegree()
    data = model.getDummyData()

    temperatures = []
    distances = []
    for i in data:
        temperatures.append(i.temp)
        distances.append(i.avgDistances)
    temperatures.sort()
    boxPlot(temperatures, distances)