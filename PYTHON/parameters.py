#########################################################################
#               EXAMPLE OF A PARAMETER FILE OF HiDES                    #
#     Author: Andres Vicente Arevalo   Date: 23-03-2020                 #
#########################################################################

# -------------- GRID PARAMETERS ----------------------------------------------
nintx = 32						# nintx number of intervals in the x direction
nintz = 32						# nintz number of intervals in the z direction
x0 = -6.; xf = 6.				# x0, xf      bounds of physical domain in the x direction
z0 = -6.; zf = 6.				# z0, zf      bounds of physical domain in the z direction

# ----------------- TIME, ITERATIONS AND PLOTS --------------------------------
itmax = 1e6						# itmax maximum number of iterations
timef = 1e2						# timef maximum physical time
plt_cad = 5; str_cad = 1e4		# plot cadence, store cadence - cadence for output
plt_type = 'contour'			# tipe of plot:   'cutx','cutz', 'contour' or 'color' 

# ----------------- INITIAL AND BOUNDARI CONDITIONS ---------------------------
itype = 'sound wave'				# itype   init. cond: (allow 20 spaces) type of initial condition betwen: 'sound wave', 'chladni', 'gaussian' 'shock' or 'packet'
shape = 'cosine'				# shape   init. cond: (allow 20 spaces) type 'gradient', 'discont' or nothing for the packet mode
rain_flag = 0					# rain_flag  a flag to activate the 'rain' option
rain_cad = 25					# rain_cad a estimate for the 'rain' cadence in relation with the iterations (integer usually from 1 to 100)
track = 0 						# track             : (allow 20 spaces) for tracking the wave paquet along the z direction
boundcond = '0deriv'			# boundcond         : (allow 20 spaces) type of boundary conditions between: 'periodic' and '0deriv' ('periodic by default')
ondx = 3.; ondz = 2.			# ondx, ondz init   : number of wave in the x and z direcction ondx = kx = 2pim/Lx and angle of the paquet angle = atan(kz/kx)
wp = 1; wt = 2					# wp  , wt          : size of the wave packet in the transversal and paralel direction to k
xc = 0.1; zc = 0.1				# xc  , zc          : point relative to the domain to start the wave packet (from 0 to 1)
nwave = 15						# nwave             : number of wave of the packet
ampl = 4e-4						# ampl       amplitude parameter 
v0_cs = 0						# v0_cs   init. equilibrium velocity or mag number in case of shock
gamm = 5./3.					# gamm :   adiabatic exponent for our gass
Um00 = 0.8						# Um00 :   value of the equilibrium density
p00 = 1.15						# p00  :   value of the equilibrium pressure

# ----------------- TIMESTEPING CRITERIA --------------------------------------
cflparam = 0.97					# cflparam   parameter for the Courant condition
