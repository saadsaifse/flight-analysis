
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
 -  datetime

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

Download the movement-analysis folder to your QGIS plugins folder and use the QGIS Plugins menu to install it. 

# Usage
  
 - Browse to the Shapefile that has to be analysed. 
![Input Interface](https://previews.dropbox.com/p/thumb/AAdc9D7sl_BcOUBZ_om_6EzQCBmflkGuYWf2cP51uqfHQ_V-w1wFxRGM9SA0L_IfLoPMKOtY2bdww6OqSbHfJX_VjwyaUgAQ58mzm9btw4ms__exvxFob8brY66PQefQzW1j0wrPjFPSUN8gHe6scBHPXZja01e2BChL80qhB3fW4zNVSCxMz-jv1l7mzWw4QPqXj0JMTKcrwTJKXdKWYU58qYqwD2aD2SVD8qqloDql-D53dNKHJGuW4ocNSloE_u93ObTwIp4hQ8NVojHrfudGOhCFpBEVcJ0p2i10s8AmExGhWmPkYhDCQ8X3AFmPZGUt-3fFLa47eAC30XuZBYyM/p.png?fv_content=true&size_mode=5)
  
 - Select the filtering parameters and click on "calculate" to see if there are any available points
![Filtering Interface](https://previews.dropbox.com/p/thumb/AAewfWAbcY6pXQnb3kMsfAxTGlnOC9jKMGgeGKIxytHsHOksACFUFlJC9CzySeStaPX4hoSP9Iv7AEJVFWQwpqgNASmm-hnwltcL99RAtQ0gXAlFjfacRImSJzTpyqSRg8xC25yUUvPKiU22eK6iljOCZu_isKW5LzaqgSC6E49fpDXz6YwwvzwO_AY5HtcOz0LDtL9JwMeA_6RmCP-Mvffj1uA5TFyVPNlYVFuLTt7ATDYmx_d3VCbXUWuDq2q1rQukxrSSDhg24yV-y7psOJ1KObnU6vIcb_FKDYyduvlyX2CrusJLPwqUlKpKCiQeQ0StncWYypdsnFeZH5DqsZ9R/p.png?fv_content=true&size_mode=5)

 - See the analysis results in three available formats by clicking on corresponding buttons to embed plots into the interface, or to see them in a popup. The popup window allows to rescale the plot, zoom in to the rectangle of interest, configure the plot parameters, and save it to the directory of choice.
![Results Interface](https://previews.dropbox.com/p/thumb/AAcUBhFroGNZmeqdI4dIeY925MjRtHcbt9UmK-rZWMPqG4rRF3wHFK3yJNWSX4YoA-YEkccNPMrZsBlaCMqxb5hnmRAjrFvlKGP78JD6y2Vnz0Acif12lyAJDgNBccf82MUsFd0EGXF1eWObzq9zXE_vAnBc5olrbhODNMN2oV0LTBRxdt7vXzLoUUXWfAr5UMde8SmyFkLWRyfQmsGSquC0vFWwssMIJoQevEEc6pGboaDloTrqpwLUBYccYID2X6yy3zBJZHHG_WHcNY3oUnhaf_b6ZSzmg2LKKcoxCK9LpbeRm7-KUQE9lUjlGOFNF_cCj_AnAGDQz80QAL5TOoZY/p.png?fv_content=true&size_mode=5)
