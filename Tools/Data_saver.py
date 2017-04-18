#Author: Damodar Rajbhandari

#!/usr/bin/python3

import os 
import numpy as np 
import matplotlib.pyplot as plot

N = 1024 #no. of spins
x = np.linspace(0.1, 4, 128)

Mean_Collect = []
for temp in x:

	with open("Data/Temp_%s.csv" %temp, "r") as infile:

		Data = infile.readlines() 
		Abs_Data = np.array([abs(float(x)) for x in Data[2:]])

		MPS = np.mean(Abs_Data/N)  # <|Magnetization|> per spin 
		Mean_Collect.append(MPS)
    	
try:
	os.mkdir("Collect")
except OSError:
	pass

np.savetxt("Collect/Collect.csv" , Mean_Collect, fmt="%f")

