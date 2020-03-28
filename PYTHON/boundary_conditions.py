# -----------------------------------------------------------------------------------
# 								ROUTINE BOUND_COND
#		Author : Andres Vicente Arevalo 	Date: 25-03-2020
#
#		PURPOSE:	Calculate the boundary conditions of a variable
#		INPUT ARGUMENTS:	
#				 typeofbc	: type of boundary conditions
#				 varr		: variable to calculate the boundary conditions (will be changed)
#
#		NOTE: 	'periodic' is the type of boundary condition.
#				In the first practical, 'periodic' is the only type used, but
#				later on you may need to add further types of boundary conditions,
#				like, zero derivative, or linear extrapolation, or zero value etc.
# ------------------------------------------------------------------------------------
from parameters import boundcond as typeofbc

def boundc(array):
	varr = array
	# compute the periodec boundary conditions either left or right
	if typeofbc == 'periodic':
		
		varr[0,:]	= varr[-2,:]
		varr[-1,:]	= varr[1,:]
		varr[:,0]	= varr[:,-2]
		varr[:,-1]	= varr[:,1]

	elif typeofbc == '0deriv':

		varr[0,:]	= varr[1,:]
		varr[-1,:]	= varr[-2,:]
		varr[:,0]	= varr[:,1]
		varr[:,-1]	= varr[:,-2]
			
	else:
		print('boundc_2d : Type of boundary conditions not properly set')
		exit()

	return varr
