# ----------------------------------------------------------------------
# 						ROUTINE PRIMITIVES
#		Author : Andres Vicente Arevalo 	Date: 25-03-2020
#
#		PURPOSE:  Calculate the primitive variables vv and pres from the
#					    mass, momentum and Uey densities.
#
#		INPUT ARGUMENTS:  ARRAYS WITH THE VALUES OF:
#						Um	: Density of matter
#						Up	: Density of momentum
#						Ue	: Density of energy
#
#		gamm (the adiabatic exponent) is passed via param module
#
#		OUTPUT:
#					 vx_z	: arrays with the velocities
#					 pres 	: array with the pressures
# ----------------------------------------------------------------------
from parameters import gamm

def dens_to_state(Um,Upx,Upz,Ue):
	
	vx	 = Upx/Um
	vz	 = Upz/Um
	pres = (gamm-1.)*(Ue - (Upx*Upx + Upz*Upz)/(2.*Um))

	return	vx,vz,pres
# ----------------------------------------------------------------------
# 							ROUTINE FLUXES
#		Author : Andres Vicente Arevalo 	Date: 25-03-2020
#
#		PURPOSE: Calculate the fluxes fmz, fpz, fez that appear in the
#				 conservation laws as functions of the densities.
#
#		INPUT ARGUMENTS: the densities Um, Up and Ue
#
#		OUTPUT:	the fluxes fmz, fpz, fez
#
# ----------------------------------------------------------------------
def dens_to_fluxes(Um,Upx,Upz,Ue):
	#compute the velocity and pressure for compute the fluxes
	vx,vz,pres = dens_to_state(Um,Upx,Upz,Ue)  

	fmx = Upx								# mass flux
	fmz = Upz
	
	fpxx = Upx*Upx/Um + pres				# momentum flux
	fpxz = Upx*Upz/Um 
	fpzz = Upz*Upz/Um + pres
	fpzx = Upz*Upx/Um 
	
	fex = (Ue + pres) * vx					# energy flux
	fez = (Ue + pres) * vz
	
	return fmx,fmz, fpxx,fpxz,fpzz,fpzx, fex,fez
