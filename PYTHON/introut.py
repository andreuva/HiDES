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
#           Um:  array with the initial values of the density
#           vx_z:  arrays with the initial values of the velocity
#           pres:array with the initial values of the pressure
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
				hz 		= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0))
				hz_vx 	= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0))*np.cos(np.arctan2(p.ondz,p.ondx))
				hz_vz 	= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0))*np.sin(np.arctan2(p.ondz,p.ondx))
			elif (p.shape == 'second mode'):
				hz 		= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0))
				hz_vx 	= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0) + np.pi)*np.cos(np.arctan2(p.ondz,p.ondx))
				hz_vz 	= np.cos(2.*np.pi*p.ondx*g.gridx/(p.xf-p.x0) + 2.*np.pi*p.ondz*g.gridz/(p.zf-p.z0) + np.pi)*np.sin(np.arctan2(p.ondz,p.ondx))
			else:
				print('ERROR : there is no type '+p.shape+' for initial conditions type '+p.itype)
				exit()

			# compute the densities and pressures with the vale of the equilibrium + the perturbation
			self.Um   = p.Um00  + p.Um00       *p.ampl*hz
			self.pres = p.p00   + p.gamm*p.p00 *p.ampl*hz
			
			# if the wave is in one axis make sure we dont have the other axis perturbation
			if (p.ondz == 0):
				self.vx   = self.v00 + self.cs00*p.ampl*hz_vx
				self.vz   = np.zeros_like(hz_vz)
			elif (p.ondx == 0):
				self.vx   = np.zeros_like(hz_vz)
				self.vz   = self.v00 + self.cs00*p.ampl*hz_vz
			else:
				self.vx   = self.v00 + self.cs00*p.ampl*hz_vx
				self.vz   = self.v00 + self.cs00*p.ampl*hz_vz

		else:
			print('ERROR : No initial conditions named '+p.itype)
			exit()

		# this calculates the sound speed array for the initial condition:
		self.cs = np.sqrt(p.gamm*self.pres/self.Um)

	def plot_ic(self, param,grid, save=True):

		fig, axs = plt.subplots(2, 2, sharex='col', sharey='row')
		(ax1, ax2), (ax3, ax4) = axs
		fig.suptitle('Pressure - Density \n Vx - Vz')
		im1 = ax1.imshow(self.pres,extent=[param.x0,param.xf,param.z0,param.zf], aspect = 'equal')
		im2 = ax2.imshow(self.Um 	,extent=[param.x0,param.xf,param.z0,param.zf], aspect = 'equal')
		im3 = ax3.imshow(self.vx 	,extent=[param.x0,param.xf,param.z0,param.zf], aspect = 'equal')
		im4 = ax4.imshow(self.vz 	,extent=[param.x0,param.xf,param.z0,param.zf], aspect = 'equal')

		fig.colorbar(im1, ax=ax1)
		fig.colorbar(im2, ax=ax2)
		fig.colorbar(im3, ax=ax3)
		fig.colorbar(im4, ax=ax4)

		for ax in axs.flat:
		    ax.label_outer()

		if save: plt.savefig('figures/initial_conditions.png')

		# plt.show()
		plt.close()

	def save_ic(self):
		np.savez('data/initial_conditions.npz', 
			pres=self.pres, Um=self.Um, vx=self.vx, vz=self.vz)
