#Author: Damodar rajbhandari

#!/usr/bin/python3

#Coding for Osager Solution's for Finding Curie Temperature.
import numpy as np
import matplotlib.pyplot as plot

x = np.linspace(0.1, 4, 128)

Tc = 2/np.log(1+np.sqrt(2))  #which is nearly equals to 2.269

OM = [] #Osager's Magnetization
for temp in x:
	if float(temp) < Tc:
		O =(1-(np.sinh(np.log(1+np.sqrt(2))*(Tc/temp)))**(-4))**(1/8)
		OM.append(O)
	elif float(temp) > Tc:
		O = 0
		OM.append(O)


plot.plot(x, OM, color = "black", marker = "*")
plot.xlabel("Temperature")
plot.ylabel("Absolute Magnetization per spin")
plot.show()


#For qtiplot software's function code: x<T ? pow(1-pow(sinh(ln(1+sqrt(2)*(T/x))),-4),1/8) : 0

