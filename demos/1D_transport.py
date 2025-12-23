import math
print("1D Linear transport")
a = input("Enter constant advection:\t")
a = float(a)
x = float(input("Enter the point of discontinuity in [0,1]:"))
print("Enter initial data for the Riemann problem:\n")
u_L = float(input("Enter u_L:\t"))
u_R = float(input("\nEnter u_R:\t"))
x_size = int(input("\nEnter grid size:\t"))
x_num = x_size - 1
T = float(input("\nEnter final time:\t"))
dt = float(input("\nEnter dt:"))
t_step_num = math.floor(T/dt)
x_grid = [] #the grid of spcae discretization
for i in range(0, x_size):
    x_grid.append((i + 0.5) * (1.0/x_num))
#initialize the Riemann initial data
def Riemann_dat(y):
    if y<x:
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
#time integration
for n in range(0, t_step_num):
    for i in range(0, x_num):
        u[i] = u[i] + a * dt * (1.0/x_size) * (u[i+1] - u[i])
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
