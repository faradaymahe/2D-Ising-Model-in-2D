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
			plot.scatter(i,j, color = 'red') # Dipole has spin up
			
		else:
			plot.scatter(i,j, color = 'black')  # Dipole has spin down
		    

plot.xlabel('x →')
plot.ylabel('y →')
plot.title('Initial configuration of our lattice')
plot.show()
