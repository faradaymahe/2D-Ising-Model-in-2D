#Author: Damodar Rajbhandari

#!/usr/bin/python3

import numpy as np 
import matplotlib.pyplot as plot 
from mpl_toolkits.mplot3d import Axes3D

n = 100
theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)

c, a = 7, 11
x = (c + a*np.cos(theta))*np.cos(phi)
y = (c + a*np.cos(theta))*np.sin(phi)
z = a*np.sin(theta)

fig = plot.figure(figsize= (10,5))
ax = fig.add_subplot(111, projection = "3d")
ax.plot_surface(x,y,z, color = "w", edgecolors = "k")

ax.set_axis_off()

plot.show()




