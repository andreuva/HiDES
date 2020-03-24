#########################################################################
#                MAIN PROGRAM OF THE HiDES PROJECT                      #
#                   2D HYDRODINAMICAL SIMULATOR                         #
#     Author: Andres Vicente Arevalo   Date: 23-03-2020                 #
#########################################################################

# import used modules
import numpy as np

# import used global variables
import introut as ic 
import grid as g


# --------------------------------------------------------------------
# 			read the initial parameters of the simulation
# --------------------------------------------------------------------
import parameters as param

# --------------------------------------------------------------------
# 			Check inconsintency in the initial parameters
# --------------------------------------------------------------------
# Check for correct intervals
if ((param.zf <= param.z0) or (param.xf <= param.x0)):
	print( 'Error: Initial points are larger than lasts ones')
	print( 'Z0 = ', param.z0, ' zf = ', param.zf)
	print( 'x0 = ', param.x0, ' xf = ', param.xf)
	exit()

if ((param.nintx <= 1) or (param.nintz <= 1)):
	print( 'Error: The Number of intervals should be 2 or greater')
	print( 'Nintx = ',param.nintx)
	print( 'Nintz = ',param.nintz)
	exit()

# make sure that the wavenumbers are integers and are lees than the lenght
ondx = int(param.ondx)
ondz = int(param.ondz)

if ((param.ondx > param.nintx) or (param.ondz > param.nintz)):
	print( 'WARNING: The Number of wave N (ond(x,z))) in k = 2pi*ond(x,z)*/L should be Nint(x,z) or smaller' )
	print( 'ondx = ',param.ondx,'	nintx = ',param.nintx)   ;   print( 'Nintz = ',param.ondz,'  nintz = ',param.nintz)
	print( 'ondx and ondz has been redefined as nintx and nintz.' )
	ondx = nintx ; ondz = nintz 

#check the boundary conditions and puts the 'periodic' as default
if ((param.boundcond != 'periodic') and (param.boundcond != '0deriv')):
	print( 'Boundari conditions "'+ param.boundcond +'" not valid, computing perodic ones as default.')
	param.boundcond = 'periodic'

#check for a warning if the stability can be compromise
if (param.cflparam >= 0.99) : print( 'WARNING: Cfl param is "',param.cflparam,'" stability may be compromised' )

# warn if no wave is selected in the wave modes
if ((param.ondx == 0) and (param.ondz == 0) and (param.itype == 'sound wave' or param.itype=='chladni' or param.itype=='packet')):
	print( 'WARNING: There are no modes selected kx=0,kz=0 : kz=1 has been set' )
	param.ondz=1

#warn if the rain is activated outside a gaussian mode or a incompatible plot mode is selected
if param.itype=='packet': param.boundcond = '0deriv'
if (param.rain_flag=='yes' and param.itype!='gaussian'): print( 'WARNING: RAIN IS ACTIVATED IN A NON GAUSSIAN MODE' )

# ---------------------------------------------------------------
# 			calculate the grid based on the parameters
# ---------------------------------------------------------------
grid = g.grid(param)
# --------------------------------------------------------------
#  				compute the initial conditions
# --------------------------------------------------------------
#the routine initrout sets up the initial condition.
init_cond = ic.introut(param,grid)   

# plot and store the initial conditions
init_cond.plot_ic(param,grid, save=True)
init_cond.save_ic()
