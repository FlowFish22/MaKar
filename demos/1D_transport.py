import math

import numpy as np
from matplotlib import pyplot as plt

import finite_volume.fvm as fvm
import finite_volume.startup as strt

print("1D Linear transport")
a = strt.speed # Constant advection
#x = 0.5  # Point of discontinuity in [0,1]
u_L, u_R = 2.0, 1.0  # Left and right values
#x_size = 50  # Grid size
#x_num = x_size - 1
T = 0.9 # Final time
dt = 1.0/1000.0  # Time-step
dx = 1/strt.x_num
t_step_num = math.floor(T / dt)
x_grid = fvm.generate_grid()


# initialize the Riemann initial data

#u = np.array([Riemann_dat(x) for x in x_grid])
u = np.where(x_grid < strt.x, u_L, u_R)

# time integration
for n in range(0, t_step_num):
    u_old = u.copy()
    for i in range(0, strt.x_num - 2):
        u[i] = u_old[i] - a * dt *(1.0/dx) * (u_old[i + 1] - u_old[i])
#   
#    for i in range(0, strt.x_num - 1):
#        u[i] = u[i] + a * dt * (1.0 / (strt.x_num - 1.0)) * (u[i + 1] - u[i])
#with open("sol.dat", "w") as sol:
#    for i in range(0, strt.x_num):
#       sl = "{}\t{}\n"
#        sol.write(sl.format(x_grid[i], u[i]))
#    sol.close()

#exact solution
u_exact = np.where(x_grid < strt.x + a * T, u_L, u_R)




f, ax = plt.subplots(layout="constrained")
ax.plot(x_grid, u, label="Computed", linestyle="-", color="b")
ax.plot(x_grid, u_exact, label="Exact", linestyle="--", color="r")
ax.set_title("Some Mainak mischief")
f.legend()
