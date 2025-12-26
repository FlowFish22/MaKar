#startup user input
import math
module = int(input('Which module?:\n' 
                ' 0 = 1D linear advenctoin'))
if module == 0:
    x_num = int(input('\n Number of mesh cells:'))
    speed = float(input('\n Enter a constant value for advection:'))
else:
    print('NA')
    quit()
init_data = int(input('\n Enter initial data:\n'
                       ' 0 = Riemann problem'))
if init_data == 0:
    x = float(input('\n Enter point of discontinuity in [0,1]:'))
else:
    print('NA')
    quit()
bdary = int(input('\nWhich bdary condn?:'
                  '\n 0 = Periodic'
                  '\n 1= other'))
if bdary != 0:
    side = int(input('\n Which side?:'
                     '\n 0 = Only left' # If only left boundary condition required
                     '\n 1 = Only right' # If only right bondary condition required
                     '\n 2 = All' )) # If boundary condition on  both the extremities are required
    
    if side == 0 or side == 1:
        condn = int(input('\n Which condition?:'
                          '\n 0 = Dirichlet'
                          '\n 1 = Neumann'))
        if condn == 0:
            bd_val = float(input('\n Enter boundary value:'))
        else:
            print('NA')
            quit()
    else:
            ls_condn = int(input('\n Left boundary condn?'
                                 '\n 0 = Dirichlet'
                                 '\n 1 = Neumann'))
            rs_condn = int(input('\n right boundary condn?'
                                 '\n 0 = Dirichlet'
                                 '\n 1 = Neumann'))
            if ls_condn == 0:
              bd_val_0 = float(input('\n Enter boundary value:'))  
            else:
                print('NA')
                quit()
            if rs_condn == 0:
              bd_val_1 = float(input('\n Enter boundary value:'))  
            else:
                print('NA')
                quit()
else:
    print('NA')
    quit()
