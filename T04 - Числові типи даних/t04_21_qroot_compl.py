#T04_21
#кількість всіх розв’язків рівняння ax**2 + bx + c = 0

import math, cmath

a = float(input('a=?'))
b = float(input('b=?'))
c = float(input('c=?'))
if a == 0 and b == 0 and c == 0:
    k = -1
elif a == 0 and b == 0:
    k = 0
elif a == 0:
    k = 1
    x1 = -c/b
else:
    k = 2
    d = b**2 - 4*a*c
    if d >=0:
        sd = math.sqrt(d)
    else:
        sd = cmath.sqrt(d)
    x1 = (-b+sd)/(2*a)
    x2 = (-b-sd)/(2*a)

if k == -1:
    print ('безліч')
elif k == 0:
    print ('немає')
elif k == 1:
    print('x1 = ', x1)
else:
    print('x1 = ', x1)
    print('x2 = ', x2)
    
              
    

