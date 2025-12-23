import math

import numpy as np
from matplotlib import pyplot as plt

import finite_volume.fvm as fvm

print("1D Linear transport")
a = 1.0  # Constant advection
x = 0.5  # Point of discontinuity in [0,1]
u_L, u_R = 1.0, 2.0  # Left and right values
x_size = 50  # Grid size
x_num = x_size - 1
T = 1.0  # Final time
dt = T / 10  # Time-step
t_step_num = math.floor(T / dt)
x_grid = fvm.generate_grid(x_size, x_num)


# initialize the Riemann initial data
def Riemann_dat(y):
    if y < x:
        return u_L
    else:
        return u_R


u = []
for i in range(0, x_size):
    u.append(Riemann_dat(x_grid[i]))
with open("init_dat.dat", "w") as init:
    for i in range(0, x_size):
        s = "{}\t{}\n"
        init.write(s.format(x_grid[i], u[i]))
    init.close()
# time integration
for n in range(0, t_step_num):
    for i in range(0, x_num):
        u[i] = u[i] + a * dt * (1.0 / x_size) * (u[i + 1] - u[i])
with open("sol.dat", "w") as sol:
    for i in range(0, x_num):
        sl = "{}\t{}\n"
        sol.write(sl.format(x_grid[i], u[i]))
    sol.close()


def Riemann_sol(y):
    if y < x + a * T:
        return u_L
    else:
        return u_R


u_exact = []
for i in range(0, x_size):
    u_exact.append(Riemann_sol(x_grid[i]))

with open("sol_exact.dat", "w") as exact:
    for i in range(0, x_num):
        ex = "{}\t{}\n"
        exact.write(ex.format(x_grid[i], u[i]))
    exact.close()

x_grid = np.array(x_grid)
u = np.array(u)
u_exact = np.array(u_exact)

f, ax = plt.subplots(layout="constrained")
ax.plot(x_grid, u, label="Computed", linestyle="--", color="b")
ax.plot(x_grid, u_exact, label="Exact", linestyle="--", color="r")
ax.set_title("Some Mainak mischief")
f.legend()
