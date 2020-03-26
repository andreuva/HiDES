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
	return, (gg[:-1,:-1] + gg[1:,:-1] + gg[:-1,1:] + gg[1:,1:])/4.
