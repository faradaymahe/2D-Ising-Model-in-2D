#Author: Damodar Rajbhandari

#!/usr/bin/python3

import numpy as np 
import matplotlib.pyplot as plot
from random import *

L = 10

"""
This represents, there are "L" (eg. 3) either in 
one row or column. Hence, 
Total sites = L*L
"""

for i in range(L):
	for j in range(L):
		if randint(0, 1) > 0.5:
			plot.scatter(i,j, color = 'black', marker = u'$\u2191$', s= 200, linewidths = 0.01) # Dipole has spin up
		
		else:
			plot.scatter(i,j, color = 'black', marker = u'$\u2193$', s= 200, linewidths = 0.01)  # Dipole has spin down
		    
		    #For more info about unicode, 
		    #see at; wikipedia.org/wiki/Template:Unicode_chart_Arrows
		    #And to increase the markersize by using s = 200 for eg.

plot.xlabel('x-axis →')
plot.ylabel('y-axis →')
plot.show()
