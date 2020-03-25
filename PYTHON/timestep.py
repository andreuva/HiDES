# ----------------------------------------------------------------------
# 								FUNCTION CFL
# 			Author : Andres Vicente Arevalo 	Date: 23-03-2020
# 
#    PURPOSE: Calculate the timestep to guarantee numerical stability
#
#    INPUT ARGUMENTS: those necessary to calculate the sound speed, namely
#           Um, Up, pres
#
#    COMMON BLOCKS: Note that some necessary input is passed via common
#                       blocks (like gamm or the grid zz)
#    OUTPUT:  the delta t
# ----------------------------------------------------------------------
import numpy as np 

def  tstep(Um,Upx,Upz,cs, param, grid):

	#compute the characteristic velocities
	vcharac1 = np.abs(np.sqrt(Upx*Upx + Upz*Upz)/Um + cs)
	vcharac2 = np.abs(np.sqrt(Upx*Upx + Upz*Upz)/Um - cs)

	#compute the proper delta t with the cflparam
	dt = param.cflparam * np.min([grid.dx,grid.dz]) / np.max([vcharac1, vcharac2])

	return dt
