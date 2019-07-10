import os
import sys
import pylab as plt

def plot(data, shouldReturn):
    """Takes formatted data and plots a boxplot

    Parameters:
        data: Two dimensional list, index 0 contains lists of temperatures, index 1 contains list of lists of avg. distances
        shouldReturn: Boolean value determining if the plot should return or show the plot. Default is plot
    """    

    plt.style.use('ggplot')
    fig = plt.figure(1)
    ax = plt.gca()
    ax.boxplot(data[1], labels=data[0])
    # set the axis labels
    ax.set_xlabel(r'$temperature$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$distance$', fontsize=14, labelpad=10, rotation=90)

    # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)

    plt.title('Distances per temperature')

    if shouldReturn:
        return plt
    
    plt.show()

if __name__ == "__main__":
    data = [
        [-10, -4, 0, 23],
        [
            [12, 56, 23, 12, 45, 67, 23, 34],
            [12, 45, 67, 23, 34, 12, 56, 23],
            [12, 45, 67, 23, 34, 12, 56, 23],
            [12, 45, 67, 23, 34, 43, 22, 22]
        ]
    ]
    plot(data)