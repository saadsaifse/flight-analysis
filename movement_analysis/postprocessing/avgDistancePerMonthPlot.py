import os
import sys
import pylab as plt

def plot(data, shouldReturn = False):
    """Takes three dimensional list of Months, Average Distances and Average temperatures and plots them

    Parameters:
        data: Three dimensional list, index 0 contains lists of months, index 1 contains lists of avg. distances while index 2 contains list of avg. temperatures
        shouldReturn: Boolean value determining if the plot should return or show the plot. Default is plot
    
    Returns:
        If shouldReturn parameter is true, then returns the Matplotlib's plt object
    """     
    yLimit = max(data[1]) + 5
    winterData = [data[0][0:2], data[1][0:2], data[2][0:2]]
    winterData[0].insert(0, data[0][11])
    winterData[1].insert(0, data[1][11])
    winterData[2].insert(0, data[2][11])
    winterData = appendTemperaturesInMonths(winterData) #dec, jan, feb
    
    springData = appendTemperaturesInMonths(
        [data[0][2:5], data[1][2:5], data[2][2:5]]) #march, april, may
    
    summerData = appendTemperaturesInMonths(
        [data[0][5:8], data[1][5:8], data[2][5:8]]) #Jun, jul, aug
    
    autumnData = appendTemperaturesInMonths(
        [data[0][8:11], data[1][8:11], data[2][8:11]]) #sep, oct, nov

    #set up 4 plots
    plt.style.use('ggplot')
    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2,2)
    fig.set_size_inches(9,6)
    fig.canvas.set_window_title('Monthly statistics of flight distances')

    #plot first graph
    ax0.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax0.bar(winterData[0], winterData[1], color='#3773FC', lw = 1)
    ax0.plot(winterData[1], color='black', alpha=0.3, linestyle='--')    
    ax0.set_ylabel(r'$avg. distance\ in\ Km$', fontsize=14, labelpad=10, rotation=90)
    ax0.tick_params(labelsize=12, length=0)
    ax0.set_title('Winters')
    ax0.set_ylim(0,yLimit)

    #plot second graph
    ax1.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax1.bar(springData[0], springData[1], color='#38D915', lw = 1)
    ax1.plot(springData[1], color='black', alpha=0.3, linestyle='--')       
    ax1.set_ylabel(r'$avg. distance\ in\ Km$', fontsize=14, labelpad=10, rotation=90)
    ax1.tick_params(labelsize=12, length=0)
    ax1.set_title('Springs')
    ax1.set_ylim(0,yLimit)
    
    #plot third graph
    ax2.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax2.bar(summerData[0], summerData[1], color='#FFE73C', lw = 1)
    ax2.plot(summerData[1], color='black', alpha=0.3, linestyle='--')
    ax2.set_xlabel(r'$month$', fontsize=14, labelpad=10)
    ax2.set_ylabel(r'$avg. distance\ in\ Km$', fontsize=14, labelpad=10, rotation=90)
    ax2.tick_params(labelsize=12, length=0)
    ax2.set_title('Summers')
    ax2.set_ylim(0,yLimit)
    
    #plot fourth graph
    ax3.grid(1, ls='--', color='#777777', alpha=0.5, lw=1)
    ax3.bar(autumnData[0], autumnData[1], color='#F1731C', lw = 1)
    ax3.plot(autumnData[1], color='black', alpha=0.3, linestyle='--')    
    ax3.set_xlabel(r'$month$', fontsize=14, labelpad=10)
    ax3.set_ylabel(r'$avg. distance\ in\ Km$', fontsize=14, labelpad=10, rotation=90)
    ax3.tick_params(labelsize=12, length=0)
    ax3.set_title('Autumns')
    ax3.set_ylim(0,yLimit)    
   
    if shouldReturn:
        return plt

    plt.show()

def appendTemperaturesInMonths(data):
    monthWithTemp = []
    for i in range(len(data[0])): #length of months list
        month = data[0][i]
        temp = data[2][i]        
        if temp != None:
            monthWithTemp.append("{} ({}°C)".format(month, str(temp)))
        else:
            monthWithTemp.append(month)
    data[0] = monthWithTemp
    return data

if __name__ == "__main__":
    data = [
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        [12, 34, 54, 66, 22, 33, 44, 66, 74, 98, 23, 45],
        [-10, -4, 0, 4, 23, 15, 32, 20, 14, 40, 14, 30]
    ]

    plot(data)