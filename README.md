
# flight-analysis

QGIS Plugin for visual analysis of correlation between air temperature and average travel distances, developed based on eagle owls data in the area of **North Rhine-Westphalia** in Germany. Any dataset can be used for analysis, as long as it contains necessary attributes, is in this study area, and contains points for years 2011-2017.

# Requirements

A default installation of QGIS3 is required, with following  libraries included:

 - PyQt5
 - qgis.core, qgis.utils
 - os
 - sys
 - processing, collections, math
 - numpy
 - pylab
 - Matplotlib
 - datetime

### Below fields must exist in the points Shapefile
 1. ind_ident: *String*
 2. timestamp: *String*
 3. lat: *Float*
 4. long: *Float*

*The temperatures dataset necessary for the analysis is provided and limited to the study area.* 
 
# Available Features
For visual analysis of the data, three kinds of plots are provided:

- Bar plot of average bird distances per seasonal months
    
- Box plots of average bird distances against temperatures
    
- Scatter plot of bird distances against temperatures with polynomial fitting

# Installation

Download the movement-analysis folder to your QGIS plugins folder and use the QGIS Plugins menu to install it. The plugin uses specifications of your QGIS to translate some of the buttons. Otherwise, the default language of the plugin is English. 

# Usage
  
 - Browse to the Shapefile that has to be analysed.  
![Input Interface](https://images2.imgbox.com/01/fd/f6Or8szl_o.png)
  
 - Select the filtering parameters and click on "calculate" to see if there are any available points.  
![Filtering Interface](https://images2.imgbox.com/2f/45/oOEYS4bW_o.png)

 - See the analysis results in three available formats by clicking on corresponding buttons to embed plots into the interface, or to see them in a popup. The popup window allows to rescale the plot, zoom in to the rectangle of interest, configure the plot parameters, and save it to the directory of choice.  
![Results Interface](https://images2.imgbox.com/71/f9/3zyfvT8T_o.png)
