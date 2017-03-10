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
#####################################################

import numpy as np
from random import *
from math import *

'''
------------------
Brief Description:
------------------

 - We're interested to study the properties of Ferromagnetic material
   with respect to its magnetization and energy at varying temperature.

 - We restrict our model in 2D, this means that there are four neighbors
   for a single spin. So, we imagine our model in the plane sheet of geometry.
   But, if you wish to work in n-dimension then, there will be 2*n neighbors.

 - At lower temperature, this materials exhibits magnetization (i.e. all spins 
   will spontaneous align themselves) even in the absence of an external magnetic 
   field. This phenonmenon is called as spontaneous magnetization.

 - But, at higher temperature, this behaviour will be destroyed. Thus, we're interested
   to find curie temperature. In other words, there's a phase transition. 

 - Ising model is usually studied in canonical ensemble. i.e. We are based in the
   "Boltzmann canonical distribution law". This law suggest, spin configurations
   with lower energies will be favored. i.e. 
   
                    ^
                    | 
                    |. 
                    | .  
                 n  |  .   n_i = A*exp(-β*E) 
                    |    .  
                    |      . 
                    |         . . . . 
                   -|------------------ >
                              E

 - We'll say "Hamiltonian" in the way along. So, don't misguided by classical 
   mechanics which uses co-ordiates(q_i) and momentum(p_i). Because the main
   essence of "Hamiltonian" is, it refers to "total energy".

 - To maximize the interaction of the spins at the edges of the lattice,
   we'll make the edges interact with the spins at the geometric opposite edges
   of the lattice. This will results a 3D torus. This concept is known as
   "Periodic Boundary Condition (PBC)".
'''

seed()  # I'll be using system current time for seed's parameter.


class Lattice:

	"""
	Creating a system of lattice. Like as,

	           1 1  1 . . .  1   1  1
	           1 1 -1 . . . -1  -1  1
	           1 1  1 . . .  1   1 -1
	           . .  . . . .  .   .  .
	           . .  . . . .  .   .  .
	           . .  . . . .  .   .  .
	           1 1 -1 . . .  1  -1  1

	such that, 1 and -1 represents the spin "up"
	and "down" respectively.
	"""

	def __init__(self, L=3):
		"""
		This represents, there are "L" (eg. 3) either in 
		one row or column. Hence, 
		   Total sites = L*L
		"""

		self.L = L

	def Initialize(self):
		"""
		Create n*n dimensional array then, in every array;
		randomly define every sites' spin.
		"""

		self.state = np.zeros((self.L, self.L))

		# Below iterations works as, filling rows one after another.

		for i in range(self.L):
			for j in range(self.L):
				if randint(0, 1) > 0.5:
					self.state[i][j] = 1  # Dipole has spin up
				else:
					self.state[i][j] = -1  # Dipole has spin down
		return self.state


'''
Now, we'll create a class for spin and, Lattice will be our inherent class. 
'''


class Spin(Lattice):

	"""
	We'll implement the "Metropolis hasting algorithm" as:
	- Start with some spin configuration. 
	- Randomly choose a spin (say, S_i). 
	- Attempt to flip it (i.e. s_i = - cs_i) [trial]
	- Compute the energy change ∆E due to this flip. 
	- If ∆E < 0, accept the trial.
	- If ∆E > 0, accept the trial with proability P = exp(-β∆E). 
	- If trial is rejected, put the spin back.
	- Again, choose another spin and follow above steps unless
	  maximum number of iterations is reached. 
      _______________________________________________________
	 |                                                       |
	 | For more detail: See http://arXiv.org/abs/0803.0217v1 |
	 |_______________________________________________________|

	"""

	def __init__(self, T = 5):
		super().__init__()
		super().Initialize() #Problem:? We use this configuration of state rather
		                     # the one was created in Lattice's class.
		self.T = T

	def Magnetization(self):
		"""
		We know, Magnetization depend upon the number of up or down spins.
		In here we'll apply, magnetization depend on the sum of
		all the spins.
		"""

		if np.sum(self.state) != 0:
			print('It can produce magnetic field !')
		else:
			print('It cannot produce magnetic field !')

		return np.sum(self.state)

	

	def Energy(self):
		"""
		First, we use PBC as;

                          ___________
                         |           |
                         | Up(i-1,j) |
              ___________|___________|____________
		     |           |           |            |
		     |left(i,j-1)|   (i,j)   |Right(i,j+1)|
		     |___________|___________|____________|
                         |           |
                         |Down(i+1,j)|
                         |___________|

		Now, we calculate the energy of a site at a particular position
		on lattice. For this, we'll go as;
		The Hamiltonian function(or,energy equation) for
		a site in absence of an external magnetic field
		is,
		    E = H(spin)= -sum((J_(ij))*(spin_i)*(spin_j)
		    where, J =J_(ij) assumed = (magnetic moment)*(Magnetic field)
		          and sum represent summation.
		
		And, J is a constant specifying the strength of interaction.
		
		If J_(ij)>0 then, the interaction is called ferromagnetic.
		
		-For our simplicity, we assume J_(ij)= J = 1. Also, we define
		 boltzmann constant, k_(β) = 1. So, beta becomes; β = 1/T.
		    
		    So, energy eqn becomes,
		          E = - sum((spin_i)*(spin_j)) 
		    E stands for energy of a single spin.
		"""

		self.E = np.zeros((self.L, self.L))

		for i in range(self.L):
			for j in range(self.L):

				n = self.L - 1
				if i == 0:  # For the state[0,j]
					top = self.state[n, j]
				else:
					top = self.state[i - 1, j]

				if i == n:  # For the state[n,j]
					bottom = self.state[0, j]
				else:
					bottom = self.state[i + 1, j]

				if j == 0:  # For the state[i,0]
					left = self.state[i, n]
				else:
					left = self.state[i, j - 1]

				if j == n:  # For the state[i,n]
					right = self.state[i, 0]
				else:
					right = self.state[i, j + 1]

				self.E[i, j] = - self.state[i, j] * (top + bottom + left + right)

		return self.E

	
	def Total_Energy(self):
		"""
		Calculating the total energy of the system.
		"""

		t = np.sum(self.E)
		return t


	def ChooseSite(self):
		"""
		This will choose one spin at random.
		"""
		self.x = randint(0, self.L - 1)
		self.y = randint(0, self.L - 1)
		self.coor = (self.x,self.y)

		self.s = self.state[self.x][self.y]
		return self.s,  self.coor , self.x , self. y


	def Flip(self):
		"""
		Choosing a spin randomly and flip it.
		"""

		if self.s == 1:
			self.state[self.x,self.y] = -1
		else:
			self.state[self.x,self.y] = 1

		self.fs = self.state[self.x,self.y]

		return self.fs


	def New_Energy(self):
		"""
		Calculating the change in energy for the flipped spin.
		This one is the interesting thing that i have done so far! 
		"""
		self.NE = self.fs*self.E[self.x,self.y]

		return self.NE

	def Change_Energy(self):
		"""
		Calculating the change in energy from new state with old state. 

		"""
		self.dE = self.NE - self.E[self.x,self.y]
		return self.dE 


	def Decision(self):
		"""
		We'll make a decision on the basis of change of energy.
		If dE<0 implies NE-E<0 i.e. NE<E. This suggests that, NE has lower
		energy than E. So, According to Boltzmann canonical distribution law;
		New state favors than previous state. 
		"""
		if self.dE < 0: 
			a = self.fs
		elif uniform(0,1)< exp(-self.dE/self.T): 
			a = self.fs
		else:
			a = self.s 
		return a


	def MC_Step(self,step=4):
		"""
		We'll have monte carlo moves to get the final configuration.
		"""
		self.step = step 

		for i in range(step):
			y.ChooseSite()
			y.Flip()
			y.New_Energy()
			y.Change_Energy()
			y.Decision()

		return self.state	






if __name__ == "__main__":
	
	# x = Lattice()
	# print(x.Initialize())
	# print(x.state)

	y = Spin()
	print('-------------------------------------------------------\n'
	 	' Welcome to world of Ising 2D Model of Ferromagnetism!\n'
	 	'-------------------------------------------------------\n')
	print('The total number of spins are %i.\n' %(y.L)**2)
	print('Our proposed configuration is:\n')
	print(y.state, '\n' )
	print('And the sum of spins is %i \n' %y.Magnetization())
	print('The energy assoicated with every sites of the spin are:')
	print('\n',y.Energy(),'\n')
	
	print('Choosing spin with site: ', y.ChooseSite())
	print('The configuration with flip spin is:')
	print(y.Flip())

	
	
	#print('Randomly choosed spin is %i.' %y.ChooseSite())
	#print('And the sum of spins is %i \n' %y.Magnetization())
	# print(y.s)
	

	print('The new energy of the fliped spin is:', y.New_Energy())
	print('The change in energy is', y.Change_Energy())

	#print('The total energy of the system is %i' %y.Total_Energy())

	print('The decision made on the basis of Metropolis Hasting Algorithm is',y.Decision())
	print('Our new configuration after Single flip spin dynamics is: ')
	print(y.state)

	print("The Final configuration is: ")
	print(y.MC_Step())
	print('And the sum of spins is %i \n' %y.Magnetization())


	