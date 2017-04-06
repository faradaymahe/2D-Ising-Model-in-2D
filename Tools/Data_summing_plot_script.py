#Author: Damodar Rajbhandari

#!/usr/bin/python3

import numpy as np 
import matplotlib.pyplot as plot

N = 256 #no. of spins
x = np.linspace(0.1, 4, 128)

Collect = []
for temp in x:

	infile = open("Data/Temp_%s.csv" %temp, "r")

	Data = infile.readlines()

	sum = 0
	for data in Data[2:]:
		sum += abs(float(data))
		
	MPS = sum/(len(Data[2:])*N) # <|Magnetization|> per spin 
	Collect.append(MPS)
	infile.close()
	del MPS

#Coding for Osager Solution's for Finding Curie Temperature.

Tc = 2/np.log(1+np.sqrt(2))  #which is nearly equals to 2.269

OM = [] #Osager's Magnetization
for temp in x:
	if float(temp) < Tc:
		O =(1-(np.sinh(np.log(1+np.sqrt(2))*(Tc/temp)))**(-4))**(1/8)
		OM.append(O)
	elif float(temp) > Tc:
		O = 0
		OM.append(O)


plot.plot(x, OM, color = "r", marker = "*", label = "Osager's formula")
plot.scatter(x,Collect, color= "black", label = "Simulation data")
plot.title("Simulation result using 256 spins")
plot.legend(loc = "best")
plot.xlabel("Temperature")
plot.ylabel("Absolute Magnetization per spin")
plot.show()

