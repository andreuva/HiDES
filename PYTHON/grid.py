# ----------------------------------------------------------------------
# 							GRID CLASS
#		Author : Andres Vicente Arevalo 	Date: 23-03-2020
#
#    PURPOSE:  Calculate the grid points based on the parameters
#    INPUT ARGUMENTS: 
#					ALL ARGUMENTS PASSED VIA param MODULE
#				x0:    lower end of the range in the x dimension
#				xf:    higher end of the range in the x dimension
# 				nintx: number of intervals in the x range
# 				z0:    lower end of the range in the z dimension
#				zf:    higher end of the range in the z dimension
# 				nintz: number of intervals in the z range
# ----------------------------------------------------------------------

import numpy as np 

class grid():
	
	def __init__(self,param):
		# compute the increments of the step in each dimension
		self.dx = (param.xf - param.x0)/param.nintx
		self.dz = (param.zf - param.z0)/param.nintz
		
		# compute the total number of points (including guard cells)
		# the points are in the center of the cells (centred lax-friedich scheme)
		self.npx = param.nintx + 2
		self.npz = param.nintz + 2

		# compute the arrays of the grid in each dimension
		self.xx = np.arange(self.npx)*self.dx + (param.x0 - (self.dx/2))
		self.zz = np.arange(self.npz)*self.dz + (param.z0 - (self.dz/2))

		# alternative way to compute the grid using purely numpy methods
		# self.xx = np.linspace( param.x0 - self.dx/2, param.xf + self.dx/2, self.npx )
		# self.zz = np.linspace( param.z0 - self.dz/2, param.zf + self.dz/2, self.npz )

		# compute the matrix grids of each dimension
		self.gridx,self.gridz = np.meshgrid(self.xx, self.zz)
		