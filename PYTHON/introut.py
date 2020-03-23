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
import parameters as param

# initialize some of the variables for the initial conditions
cs00 = np.sqrt(param.gamm * param.p00 /param.Um00)
v00 = param.v0_cs*cs00

