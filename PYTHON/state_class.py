class state():

	def __init__(self, param, init_cond):
		# initialice the variables of the loop with the initial conditions
		self.vx    	= init_cond.vx
		self.vz   	= init_cond.vz
		self.cs  	= init_cond.cs
		self.pres 	= init_cond.pres
		self.Um    	= init_cond.Um
		# this calculates the initial values of the 'densities' for momentum and energy:
		self.Ue   	= init_cond.pres/(param.gamm-1.) + init_cond.Um*(init_cond.vx**2. + init_cond.vz**2.)/2.
		self.Upx  	= init_cond.vx*init_cond.Um
		self.Upz  	= init_cond.vz*init_cond.Um
		self.Umn	= self.Um
		self.Upxn	= self.Upx
		self.Upzn	= self.Upz
		self.Uen	= self.Ue

		