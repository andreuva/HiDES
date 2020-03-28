# --------------------------------------------------------------------------------
# 								ROUTINE ADVANCE
# 			Author : Andres Vicente Arevalo 	Date: 26-03-2020
# 
#		PURPOSE:	Calculate variables at timestep n+1.
#					this routine contains the numerical scheme used in the code.
#
#		INPUT ARGUMENTS:	- the densities at timestep n, namely Um, Up, Ue
#							- the fluxes fmz, fpz, fez
#
#		COMMON BLOCKS: 	Note that some necessary input is passed via common
#						blocks (like the grid parameters and array zz, etc)
#
#		OUTPUT:	the densities at timestep n+1, namely Umn, Upx_zn , Uen
# --------------------------------------------------------------------------------
import derivates as d 
import conversions as conv

def advance(dt, grid,	Um,Upx,Upz,Ue, fmx,fmz,	 fpxx,fpxz,fpzz,fpzx,	fex,fez):
	
	# initialice the variables of the next iteration (n=new)
	Umn = Um; 	Uen = Ue; 	Upxn = Upx; 	Upzn = Upz 

	fmxdx	=	d.deriv2d(fmx, grid, axes='x')
	fmzdz	=	d.deriv2d(fmz, grid, axes='z')
	fexdx	=	d.deriv2d(fex, grid, axes='x')
	fezdz	=	d.deriv2d(fez, grid, axes='z')
	fpxxdx	=	d.deriv2d(fpxx, grid, axes='x')
	fpzzdz	=	d.deriv2d(fpzz, grid, axes='z')
	fpzxdx	=	d.deriv2d(fpzx, grid, axes='x')
	fpxzdz 	=	d.deriv2d(fpxz, grid, axes='z')
	
	# compute the densities in the time t + dt/2
	Umn[:-1,:-1]	= d.midval(Um)	- (dt/2)*(fmxdx	 + fmzdz)
	Uen[:-1,:-1]	= d.midval(Ue)	- (dt/2)*(fexdx	 + fezdz)
	Upxn[:-1,:-1]	= d.midval(Upx) - (dt/2)*(fpxxdx + fpxzdz)
	Upzn[:-1,:-1]	= d.midval(Upz) - (dt/2)*(fpzzdz + fpzxdx)

	# calculate the fluxes in t + dt/2
	fmxn,fmzn, fpxxn,fpxzn,fpzzn,fpzxn, fexn,fezn = conv.dens_to_fluxes(Umn[:-1,:-1],Upxn[:-1,:-1],Upzn[:-1,:-1],Uen[:-1,:-1])

	fmxdx	=	d.deriv2d(fmxn, grid, axes='x')
	fmzdz	=	d.deriv2d(fmzn, grid, axes='z')
	fexdx	=	d.deriv2d(fexn, grid, axes='x')
	fezdz	=	d.deriv2d(fezn, grid, axes='z')
	fpxxdx	=	d.deriv2d(fpxxn, grid, axes='x')
	fpzzdz	=	d.deriv2d(fpzzn, grid, axes='z')
	fpzxdx	=	d.deriv2d(fpzxn, grid, axes='x')
	fpxzdz 	=	d.deriv2d(fpxzn, grid, axes='z')
	
	# compute the densities in the time t + dt 
	Umn[1:-1,1:-1] 	= Um[1:-1,1:-1]  - dt*(fmxdx  + fmzdz)
	Uen[1:-1,1:-1] 	= Ue[1:-1,1:-1]  - dt*(fexdx  + fezdz)
	Upxn[1:-1,1:-1] = Upx[1:-1,1:-1] - dt*(fpxxdx + fpxzdz)
	Upzn[1:-1,1:-1] = Upz[1:-1,1:-1] - dt*(fpzzdz + fpzxdx)

	return Umn,Upxn,Upzn,Uen
