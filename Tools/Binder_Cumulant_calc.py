#Author: Damodar Rajbhandari 

#!/usr/bin/python3

import numpy as np 
import matplotlib.pyplot as plot

x = np.linspace(0.1, 4, 128)

Cumulant = []
for temp in x:

	with open("Data/Temp_%s.csv" %temp, "r") as infile:

		Data = infile.readlines() 
		M4 = np.array([(float(x))**4 for x in Data[2:]])
		M2 = np.array([(float(x))**2 for x in Data[2:]])

		MM4 = np.mean(M4)  
		MM2 = np.mean(M2)

		U = 1- (MM4)/(3*(MM2**2))

		Cumulant.append(U)
		
import os 
	
try:
	os.mkdir("Cumulant")
except OSError:
	pass

np.savetxt("Cumulant/Cumulant.csv" , Cumulant, fmt="%f")

