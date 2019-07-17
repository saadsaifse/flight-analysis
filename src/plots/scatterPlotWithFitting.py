import os
import sys
import pylab as plt
import numpy as np

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

def scatterPlot(data):
    # Showing multiple boxplots on the same window
    plt.style.use('ggplot')
    
    #colors = getColorsForTemperaturesRange(temperatures)
    
    plt.scatter(data[0], data[1])
    axes = plt.gca()
    m, b = np.polyfit(data[0], data[1], 1)
    x_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(x_plot, m * x_plot + b, '-')

    # set the axis labels
    axes.set_xlabel(r'$temperature$', fontsize=14, labelpad=10)
    axes.set_ylabel(r'$distance$', fontsize=14, labelpad=10, rotation=90)

     # Customize the plot
    axes.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    axes.tick_params(labelsize=12, length=0)
    
    plt.title("Bird scatter plot")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    data = [
            [-10, -4, 0, 23, -4, 10, 23, 34, 12, 98],
            [12, 45, 67, 23, 34, 43, 22, 22, 49, 84]
        ]
    scatterPlot(data)