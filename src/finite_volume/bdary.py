import math
import numpy as np
import finite_volume.startup as strt
#periodic bdary condition
def per_bd(a):
    y = np.zeros(len(a) + 1) #one layers of ghost cell on each side
    #y[-1] += a[0] #right boundary
    y[0] += a[-1] #left boundary
    y[:-2] += a
    return y
def bd(x):
    if strt.bdary == 0:
        a = per_bd(x)
        return a
    else:
        print('NA')
        return 0
