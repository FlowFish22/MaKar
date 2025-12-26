import math
import numpy as np
import finite_volume.startup as strt
#periodic bdary condition
def per_bd(a):
    y = np.zeros(len(a) + 2) #one layers of ghost cell on each side
    y[-1] += a[0] #ghost cell with the right boudary take value from the first domain cell on the left
    y[0] += a[-1] #ghost cell with the left boundary take value from the last domain cell on the right
    y[1:-1] += a
    return y
def dir_bd(a):
    ed = strt.side
    if ed == 0:
        y = np.zeros(len(a) + 1) #adding one layer of ghost cell on one side
        y[0] += strt.bd_val
        y[1:] += a
    elif ed == 1:
        y = np.zeros(len(a) + 1) #adding one layer of ghost cell on one side
        y[-1] += strt.bd_val
        y[:-1] += a
    elif ed == 2:
        y = np.zeros(len(a) + 2) #adding one layer of ghost cells on both sides
        y[0] += strt.bd_val_0
        y[-1] += strt.bd_val_1
        y[1:-1] += a
    return y
def bd(x):
    if strt.bdary == 0:
        y = per_bd(x)
        return y
    else:
        y = dir_bd(x)
        return y
