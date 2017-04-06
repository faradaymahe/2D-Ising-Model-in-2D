#####################################################
# Author: Damodar Rajbhandari                       #
# Work: Ising Model in two dimension                #
# Strategies: Lattice and Spin Model                #
# Object: Ferromagnetic material                    #
# Aim: To show, there's a phase transition in 2-D   #
#      And, To calculate the Curie temperature      #
#      (i.e. Critical Temperature)                  #
# Version: Python v.3.5                             #
# Programming Approach: Object Oriented Programming #
# Acknowledgement: I would like to thank to my      #
#                  advisor Jonah Maxwell Miller     #
#                  for invaluable guidance on       # 
#                  helping me to optimize this code.#                       
#####################################################

#!/usr/bin/python3
 
import numpy as np
from numpy.random import *

seed()  # I'll be using system current time for seed's parameter.


class Ising():

	"""
	Implementing the Ising 2D model!
	"""

	def __init__(self, L, temp):
		"""
		This represents, there are "L" (eg. 3) either in 
		one row or column. Hence, 
		   Total sites = L*L
		"""

		self.L = L
		self.T = temp

	
	def Initialize(self):
		"""
		Creating a system of lattice with spin configuration. 
		"""

		self.state = np.zeros((self.L, self.L))

		# Below iterations works as, filling rows one after another.

		for i in range(self.L):
			for j in range(self.L):
				if randint(0, 2) > 0.5:
					self.state[i][j] = 1  # Dipole has spin up
				else:
					self.state[i][j] = -1  # Dipole has spin down
		return self.state


	def Energy_Calc(self):
		"""
		Calculate energy of each spins and implemented Periodic Boundary Condition.
		"""
		self.E = np.zeros((self.L, self.L))

		#Taking care of spins except edges and corners i.e.  center = center*(top+bottom+left+right)
		self.E[1:-1,1:-1] = -self.state[1:-1,1:-1]*(self.state[2:,1:-1]+self.state[:-2,1:-1]+self.state[1:-1,:-2]+self.state[1:-1,2:])

		#Taking care of edges
		#Left
		self.E[1:-1,0] = -self.state[1:-1,0]*(self.state[2:,-1]+self.state[:-2,-1]+self.state[1:-1,-1]+self.state[1:-1,2])

		#right
		self.E[1:-1,-1] = -self.state[1:-1,0]*(self.state[2:,-1]+self.state[:-2,-1]+self.state[1:-1,-2]+self.state[1:-1,0])

		#top
		self.E[-1,1:-1] = -self.state[-1,1:-1]*(self.state[0,1:-1]+self.state[-2,1:-1]+self.state[-1,:-2]+self.state[-1,2:])

		#bottom
		self.E[0,1:-1] = -self.state[0,1:-1]*(self.state[1,1:-1]+self.state[-1,1:-1]+self.state[0,:-2]+self.state[0,2:])

		#take care of corners, which must be handled manually
		
		#bottom left
		self.E[0,0] = -self.state[0,0]*(self.state[1,0]+self.state[-1,0]+self.state[0,-1]+self.state[0,1])
		
		#bottom right
		self.E[0,-1] = -self.state[0,-1]*(self.state[1,-1]+self.state[-1,-1]+self.state[0,-2]+self.state[0,0])
		
		#top left
		self.E[-1,0] = -self.state[-1,0]*(self.state[0,0]+self.state[-2,0]+self.state[-1,-1]+self.state[-1,1])
		
		#top right
		self.E[-1,-1] = -self.state[-1,-1]*(self.state[0,-1]+self.state[-2,-1]+self.state[-1,-2]+self.state[-1,0])

		return self.E


	def Choose_Spin(self):
		"""
		This will choose one spin at random and calculate its energy.
		"""
		self.x = randint(0, self.L)
		self.y = randint(0, self.L)

		self.s = self.state[self.x, self.y]
		self.LE = self.E[self.x, self.y]

		return self.s , self.LE


	def Flip(self):
		"""
		Flip the choosed spin and calculate its new energy. 
		"""

		if self.s == 1:
			self.state[self.x,self.y] = -1
		else:
			self.state[self.x,self.y] = 1

		self.fs = self.state[self.x,self.y]
		

		return self.fs

	def New_Energy(self):
		"""
		Calculating the new energy of that spin
		"""
		if self.fs == 1:
			self.NE = -self.fs*self.LE 
		else:
			self.NE = self.fs*self.LE

		return self.NE


	def Change_Energy(self):
		"""
		Calculating the change in energy for the flipped spin. 
		"""
		self.dE = self.NE - self.LE

		return self.dE 

	

	def Decision(self):
		"""
		We'll make a decision on the basis of change of energy. 
		"""
		if self.dE < 0: 
			self.state[self.x,self.y] = self.fs
		elif uniform(0,1)< np.exp(-self.dE/self.T): 
			self.state[self.x,self.y] = self.fs
		else:
			self.state[self.x,self.y] = self.s 
		return self.state[self.x,self.y]


	def Magnetization(self):
		"""
		We know, Magnetization depend upon the number of up or down spins.
		In here we'll apply, magnetization depend on the sum of
		all the spins.
		"""
		return np.sum(self.state)


	def MC_Step(self, step=2000):
		"""
		We'll have monte carlo moves to get the final configuration.
		"""
		self.step = step 

		for i in range(step):
			y.Energy_Calc()
			y.Choose_Spin()
			y.Flip()
			y.New_Energy()
			y.Change_Energy()
			y.Decision()
			

		return y.Magnetization()	


if __name__ == "__main__":

	import os 
	
	try:
		os.mkdir("Data")
	except OSError:
		pass

	

	for temp in np.linspace(0.1, 4, 128):
		
		y = Ising(16, temp)
		y.Initialize()
		
		Mag_Data = [ ]
		for i in np.arange(500):	

			Mag = y.MC_Step()
			Mag_Data.append(Mag)
	
		#Below command will save the data from the simulation 
		title = "Magnetization on running the simulation \n for x times under similar condition"
		np.savetxt("Data/Temp_%s.csv" %temp , Mag_Data, fmt="%i", header = title) 
		
