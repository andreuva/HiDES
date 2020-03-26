# --------------------------------------------------------------------------------
#									ROUTINE DERIV2D
#			 	Author : Andres Vicente Arevalo	 Date: 26-03-2020
#
#		PURPOSE: Calculate the X and Z derivates for a matrix
#	
#		INPUT ARGUMENTS: gg :matrix with arbitrary dimensions
#
#		OUTPUT: derx,derz : the derivates in either x or z directions 
#
# ---------------------------------------------------------------------------------
def deriv2d(gg, grid , axes = 'xz'):

	if (axes != 'x' and axes != 'z' and axes != 'xz'):
		print('deriv2d warning: axes'+axes+'not valid, switching to default x and z')
	
	#compute the x or z derivates in each case or raise a error if the function is not properly call.
	if axes == 'x':
		derx = ((gg[1:,:-1] - gg[:-1,:-1])/grid.dx + (gg[1:,1:] - gg[:-1,1:])/grid.dx )/2.
		return derx
	elif axes == 'z':
		derz = ((gg[:-1,1:] - gg[:-1,:-1])/grid.dz + (gg[1:,1:] - gg[1:,:-1])/grid.dz )/2.
		return derz
	else:
		derx = ((gg[1:,:-1] - gg[:-1,:-1])/grid.dx + (gg[1:,1:] - gg[:-1,1:])/grid.dx )/2.
		derz = ((gg[:-1,1:] - gg[:-1,:-1])/grid.dz + (gg[1:,1:] - gg[1:,:-1])/grid.dz )/2.
		return derx,derz

# -------------------------------------------------------------------------------
# 							ROUTINE MIDVAL
# 			Author : Andres Vicente Arevalo 	Date: 26-03-2020
# 
#    PURPOSE: Calculate the averages of four neighbours grid points
#
#    INPUT ARGUMENTS: gg :matrix with arbitrary dimensions
#
#    OUTPUT: mid : a matrix with the mean of the 4 neiborg points
# --------------------------------------------------------------------------------
def midval(gg):
	return (gg[:-1,:-1] + gg[1:,:-1] + gg[:-1,1:] + gg[1:,1:])/4.