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
    
