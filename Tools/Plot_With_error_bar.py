import numpy as np 
import matplotlib.pyplot as plot

N = 256 #no. of spins
x = np.linspace(0.1, 4, 128)

Mean_Collect = []
Std_Collect = []
for temp in x:

	with open("Data/Temp_%s.csv" %temp, "r") as infile:


		Data = infile.readlines() 

		Abs_Data = np.array([abs(float(x)) for x in Data[2:]])

		MPS = np.mean(Abs_Data/N)  # <|Magnetization|> per spin 
		STDPS = np.std(Abs_Data[2:]/N) # standard deviation per spin
		Mean_Collect.append(MPS)
		Std_Collect.append(STDPS)


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
plot.errorbar(x,Mean_Collect, yerr = Std_Collect, color= "black", fmt = "o", label = "Simulation Data")
plot.title("Simulation result using 256 spins")
plot.legend(loc = "best")
plot.xlabel("Temperature")
plot.ylabel("Absolute Magnetization per spin")
plot.show()

