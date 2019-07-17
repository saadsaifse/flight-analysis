import os
import sys
import matplotlib.pylab as plt
# from matplotlib.pyplot import figure


def plot(data, shouldReturn = False):
    """Takes formatted data and plots a boxplot

    Parameters:
        data: Two dimensional list, index 0 contains lists of temperatures, index 1 contains list of lists of avg. distances
        shouldReturn: Boolean value determining if the plot should return or show the plot. Default is plot
    
    Returns:
        If shouldReturn parameter is true, then returns the Matplotlib's plt object
    """    
    plt.clf()
    plt.style.use('ggplot')
    fig = plt.figure(1)
    fig.set_size_inches(9, 6)

    ax = plt.gca()
    ax.boxplot(data[1], labels=data[0])
    # set the axis labels
    ax.set_xlabel(r'$temperature\ °C$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$distance\ in\ kilometers$', fontsize=14, labelpad=10, rotation=90)

    # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)

    plt.title('Distances per temperature')
    fig.canvas.set_window_title('Average distance per temperature plot')

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