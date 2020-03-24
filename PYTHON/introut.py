# ----------------------------------------------------------------------
# 							ROUTINE INITROUT
#		Author : Andres Vicente Arevalo 	Date: 23-03-2020
#
#    PURPOSE:  Calculate the arrays of density, velocity and pressure
#                 at time t=0.
#    INPUT ARGUMENTS: 
#           itype:   char variable with the choice of initial condition
#           shape:   char variable with some subsidiary choice
#           ampl :   amplitud of the pertubation
# 			gamm :   adiabatic exponent for our gass
# 			Um00 :   value of the equilibrium density
#           p00  :   value of the equilibrium pressure
#           v0_cs:   value in wich v00 is prop to cs00
#        GRID:
#           z0, zf:  inital and final values of the z range
#           x0, xf:  inital and final values of the x range
#        NONSPEC COMMON
#              
#    OUTPUT:  VIA INIT_C COMMON:
#           cs00 :   value of the speed of sound in equilibrium
#           v00  :   value of the equilibrium velocity 
#           Uminit:  array with the initial values of the density
#           vvinit:  array with the initial values of the velocity
#           presinit:array with the initial values of the pressure
# ----------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


class introut():

	# p = param (parameters of the simulation in a the module parameters.py)
	# g = grid (grid object initialice with the parameters)
	def __init__(self, p,g):

		# initialize some of the underlying variables for the initial conditions
		self.cs00 	= np.sqrt(p.gamm * p.p00 /p.Um00)
		self.v00 	= p.v0_cs*self.cs00

		# choose the right type of initial perturbation
		if (p.itype == 'sound wave'):
			# if its a sound wave compute the initial conditions with a cosine
			# or if it's the second mode, a cosine + a phase in the velocity
			if (p.shape == 'cosine'):

				hz 		= np.cos(2*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2*np.pi*p.ondz*g.gridz/(p.zf-p.z0))
				hz_vx 	= np.cos(2*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2*np.pi*p.ondz*g.gridz/(p.zf-p.z0))*np.cos(np.arctan(p.ondz/p.ondx))
				hz_vz 	= np.cos(2*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2*np.pi*p.ondz*g.gridz/(p.zf-p.z0))*np.sin(np.arctan(p.ondz/p.ondx))
				
				# compute the densities and pressures with the vale of the equilibrium + the perturbation
				self.Uminit   = p.Um00  + p.Um00       *p.ampl*hz
				self.presinit = p.p00   + p.gamm*p.p00 *p.ampl*hz
				
				# if the wave is in one axis make sure we dont have the other axis perturbation
				if (p.ondz == 0):
					self.vxinit   = self.v00 + self.cs00*ampl*hz_vx
					self.vzinit   = np.zeros_like(hz_vz)
				elif (p.ondx == 0):
					self.vxinit   = np.zeros_like(hz_vz)
					self.vzinit   = self.v00 + self.cs00*p.ampl*hz_vz
				else:
					self.vxinit   = self.v00 + self.cs00*p.ampl*hz_vx
					self.vzinit   = self.v00 + self.cs00*p.ampl*hz_vz

		# this calculates the sound speed array for the initial condition:
		self.csinit = np.sqrt(p.gamm*self.presinit/self.Uminit)

	def plot_ic(self, param,grid, save=True):
		
		plt.figure()
		plt.imshow(self.presinit)

		if save:
			print('saving plot')
		plt.show()

	def save_ic(self):
		print('save_ic...')
