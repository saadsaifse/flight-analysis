import os
import sys

modelsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../models')
print(modelsPath)
sys.path.append(modelsPath)

import pylab as plt
from scatterPlotModel import ScatterPlotModel
from enums import Season

from matplotlib.lines import Line2D


def getColorsForTemperaturesRange(temperatures):
    colors = []
    for t in temperatures:
        if (t in range(-99, 15)):
            colors.append('white')
        elif (t in range(15, 25)):
            colors.append('green')
        elif (t in range(25, 40)):
            colors.append('yellow')
        else:
            colors.append('black')
    return colors

def scatterPlot(birdId, latitudes, longitudes, temperatures):
    # Showing multiple boxplots on the same window
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    colors = getColorsForTemperaturesRange(temperatures)
    ax.scatter(latitudes, longitudes, c=colors)
    
    #set legend
    custom_lines = [Line2D([0], [0], marker = 'o', markerfacecolor='white', label='-99 >= t < 15', markersize=10),
                    Line2D([0], [0], marker = 'o', markerfacecolor='green', label='15 >= t < 25', markersize=10),
                    Line2D([0], [0], marker = 'o', markerfacecolor='yellow', label='25 >= t < 40', markersize=10),
                    Line2D([0], [0], marker = 'o', markerfacecolor='black', label='40 >= t', markersize=10)]
    ax.legend(handles=custom_lines)
    
    # set the axis labels
    ax.set_xlabel(r'$latitude$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$longitude$', fontsize=14, labelpad=10, rotation=90)

     # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)    
    plt.title("Bird scatter plot")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    model = ScatterPlotModel()
    data = model.getDummyDataSingleBird()    
    scatterPlot(data.birdId, data.latitudes, data.longitudes, data.temperatures)