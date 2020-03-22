#########################################################################
#                MAIN PROGRAM OF THE HiDES PROJECT                      #
#                   2D HYDRODINAMICAL SIMULATOR                         #
#     Author: Andres Vicente Arevalo   Date: 22-03-2020                 #
#########################################################################

# import used global variables
#import ........

# import used modules
import numpy as np

# ----------------------------------------------
# read the initial parameters of the simulation
from parameters import *

# ---------------------------------------------
#calculate the grid based on the parameters
dx = (xf-x0)/nintx
dz = (zf-z0)/nintz

xx = np.arange(npx)*dx + (x0 - (dx/2))
zz = np.arange(npz)*dz + (z0 - (dz/2))

#gridx = xx#(dblarr(npz)+1)
#gridz = (dblarr(npx)+1)#zz

# ---------------------------------------------
