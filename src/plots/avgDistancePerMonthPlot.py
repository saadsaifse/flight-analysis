import os
import sys
import pylab as plt

def plot(data):
    """Takes three dimensional list of Months, Average Distances and Average temperatures and plots them

    Parameters:
        data: Three dimensional list, index 0 contains lists of months, index 1 contains lists of avg. distances while index 2 contains list of avg. temperatures
    """    

    plt.style.use('ggplot')
    fig = plt.figure(1)
    ax = plt.gca()
    ax.bar(data[0], data[1], lw = 1)
    ax.plot(data[1], color='black', alpha=0.3, linestyle='--')
    # set the axis labels
    ax.set_xlabel(r'$month$', fontsize=14, labelpad=10)
    ax.set_ylabel(r'$avg. distance$', fontsize=14, labelpad=10, rotation=90)

    # Customize the plot
    ax.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax.tick_params(labelsize=12, length=0)

    plt.title('Average distances per month')
    plt.show()

if __name__ == "__main__":
    data = [
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        [12, 34, 54, 66, 22, 33, 44, 66, 74, 98, 23, 45],
        [-10, -4, 0, 4, 23, 15, 32, 20, 14, 40, 14, 30]
    ]
    monthWithTemp = []
    for i in range(12):
        month = data[0][i]
        temp = data[2][i]
        if temp != None:
            monthWithTemp.append("{} ({}°C)".format(month, str(temp)))
    
    data[0] = monthWithTemp

    plot(data)