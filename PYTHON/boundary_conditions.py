# -----------------------------------------------------------------------------------
# 								ROUTINE BOUND_COND
#		Author : Andres Vicente Arevalo 	Date: 25-03-2020
#
#		PURPOSE:	Calculate the boundary conditions of a variable
#		INPUT ARGUMENTS:	
#				 typeofbc	: type of boundary conditions
#				 site		: direcction in wich the boundary conditions are going to be set
#				 varr		: variable to calculate the boundary conditions (will be changed)
#	
#		OUTPUT:	The output is preformed via input arguments changing varr variable
#
#		NOTE: 'left' and 'right' below refer to the respective limits of the domain.
#				'periodic' is the type of boundary condition.
#				In the first practical, 'periodic' is the only type used, but
#				later on you may need to add further types of boundary conditions,
#				like, zero derivative, or linear extrapolation, or zero value etc.
# ------------------------------------------------------------------------------------
from parameters import boundcond as typeofbc

def boundc(site,varr):

	# compute the periodec boundary conditions either left or right
	if typeofbc == 'periodic':
		
		if site == 'left':
			varr[0,:]	= varr[-2,:]
		elif site == 'right':
			varr[-1,:]	= varr[1,:]
		elif site == 'down':
			varr[:,0]	= varr[:,-2]
		elif site == 'up':
			varr[:,-1]	= varr[:,1]
		else:
			print('boundc_2d.pro: Periodic boundary conditions should be left, right, up or down')

	elif typeofbc == '0deriv':
		
		if site == 'left':
			varr[0,:]	= varr[1,:]
		elif site == 'right':
			varr[-1,:]	= varr[-2,:]
		elif site == 'down':
			varr[:,0]	= varr[:,1]
		elif site == 'up':
			varr[:,-1]	= varr[:,-2]
		else:
			print, 'boundc_2d.pro: 0deriv boundary conditions should be left, right, up or down'
			
	else:
		print, 'boundc_2d : Type of boundary conditions not properly set'

	return varr
