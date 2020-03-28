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
from timestep import tstep
import conversions as convers
from boundary_conditions import boundc
from advance import advance
import representation as rp
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

if ((param.ondx > param.nintx) or (param.ondz > param.nintz)):
	print( 'WARNING: The Number of wave N (ond(x,z))) in k = 2pi*ond(x,z)*/L should be Nint(x,z) or smaller' )
	print( 'ondx = ',param.ondx,'	nintx = ',param.nintx)   ;   print( 'ondz = ',param.ondz,'  nintz = ',param.nintz)
	print( 'ondx and ondz has been redefined as nintx and nintz.' )
	param.ondx = param.nintx ; param.ondz = param.nintz 
	print( 'ondx = ',param.ondx,'	nintx = ',param.nintx)   ;   print( 'ondz = ',param.ondz,'  nintz = ',param.nintz)

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
# init_cond.save_ic()
# ------------------------------------------------------------
# 			declare and/or initialize variables
# ------------------------------------------------------------
# initialice the variables of the loop with the initial conditions
vx    	= init_cond.vx
vz   	= init_cond.vz
cs  	= init_cond.cs
pres 	= init_cond.pres
Um    	= init_cond.Um
# this calculates the initial values of the 'densities' for momentum and energy:
Ue   	= init_cond.pres/(param.gamm-1.) + init_cond.Um*(init_cond.vx**2. + init_cond.vz**2.)/2.
Upx  	= init_cond.vx*init_cond.Um
Upz  	= init_cond.vz*init_cond.Um
# the 'densities', in the sense of the conservation laws,
#      are 'Um', 'Upx', 'Upz' and  'Ue'.

itt  = 0
time = 0.

# ------------------------------------------------------------
# 						MAIN LOOP
# ------------------------------------------------------------
while (itt < param.itmax and time < param.timef):

#	CALCULATE FLUXES FROM DENSITIES ('fluxes' is the name of the subroutine)
	fmx,fmz, fpxx,fpxz,fpzz,fpzx, fex,fez = convers.dens_to_fluxes(Um,Upx,Upz,Ue)

#	TIMESTEP
	dt=tstep(Um,Upx,Upz,cs, param, grid)
	print('time = ',np.round(time,3) ,'\t itterations = ',itt,'\t dt = ',dt)
	if ((time+dt) > param.timef):
		dt = param.timef-time

#	ADVANCE ONE TIMESTEP using the chosen numerical scheme 
	Umn,Upxn,Upzn,Uen = advance(dt, grid, Um,Upx,Upz,Ue,fmx,fmz,fpxx,fpxz,fpzz,fpzx,fex,fez)

#	BOUNDARY CONDITIONS
	Umn = boundc(Umn)
	Uen = boundc(Uen)
	Upxn = boundc(Upxn)
	Upzn = boundc(Upzn)

#	CALCULATE PRIMITIVE VARIABLES FROM THE DENSITIES
	vxn,vzn,presn = convers.dens_to_state( Umn,Upxn,Upzn,Uen)

#	EXCHANGE NEW AND OLD VARIABLES
	Um = Umn; Upx = Upxn; Upz = Upzn; Ue = Uen;
	pres = presn; vx = vxn; vz = vzn 

	itt += 1      # advance itterations
	time += dt # advance time

#   PLOT RESULTS
	if (itt%param.plt_cad == 0 or itt == 0 or time >= param.timef) :      

		if param.plt_type == 'cutz':
			vv = np.sqrt(vx*vx + vz*vz)
			# rp.drawing(Um[int(npx/2),:],pres[int(npx/2),:],vv[int(npx/2),:],grid.xx)
		elif param.plt_type == 'cutx':
			vv = sqrt(vx*vx + vz*vz)
			# rp.drawing(Um[:,int(npz/2)],pres[:,int(npz/2)],vv[:,fix(npz/2)],grid.zz)
		else :
			rp.drawing_2d(init_cond, param, Um,pres,vx,vz, time, itt, dt)
# ------------------------------------------------------------
# 		END OF BIG LOOP -- RESULTS AND LAST OUTPUTS
# ------------------------------------------------------------
print('\n PROGRAM FINISHED !!\n'+\
	'itt\t\t=\t'+ str(itt) +'\n'+\
	'time\t=\t'+ str(time) +'\n')
