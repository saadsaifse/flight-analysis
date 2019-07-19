import os
import sys
import pylab as plt
import numpy as np

from matplotlib.lines import Line2D

def scatterPlot(data, shouldReturn = False):
    """Takes formatted data and plots a scatterplot

    Parameters:
        data: Two dimensional list, index 0 contains lists of temperatures while index 1 contains list of distances
        shouldReturn: Boolean value determining if the plot should return or show the plot. Default is plot
    
    Returns:
        If shouldReturn parameter is true, then returns the Matplotlib's plt object
    """

    plt.clf()
    plt.style.use('ggplot')

    fig = plt.figure(1)
    fig.set_size_inches(9, 6)
      
    plt.scatter(data[0], data[1])
    axes = plt.gca()
    m, b = np.polyfit(data[0], data[1], 1)
    x_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
    plt.plot(x_plot, m * x_plot + b, '-')

    # set the axis labels
    axes.set_xlabel(r'$temperature\ °C $', fontsize=14, labelpad=10)
    axes.set_ylabel(r'$distance\ in\ kilometers$', fontsize=14, labelpad=10, rotation=90)

     # Customize the plot
    axes.grid(1, ls='--', color='k', alpha=0.5, lw=1)
    axes.tick_params(labelsize=12, length=0)
    
    plt.title("Distances travelled vs temperature")
    fig.canvas.set_window_title('Temperature vs distance scatter plot')
    # plt.axis('equal')
    if shouldReturn:
        return plt
    plt.show()

if __name__ == "__main__":
    data = [
        [-10, -4, 0, 23, -4, 10, 23, 34, 12, 98],
        [12, 45, 67, 23, 34, 43, 22, 22, 49, 84]
        ]  
    scatterPlot(data)