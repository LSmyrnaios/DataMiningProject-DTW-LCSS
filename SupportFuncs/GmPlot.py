import gmplot
import numpy as np


def gmPlot(latitudes, longtitutes, fileName):

    gmap = gmplot.GoogleMapPlotter(np.mean(latitudes), np.mean(longtitutes), 12)

    gmap.plot(latitudes, longtitutes, 'cornflowerblue', edge_width=10)
    gmap.draw("Resources/maps/" + fileName + ".html")
