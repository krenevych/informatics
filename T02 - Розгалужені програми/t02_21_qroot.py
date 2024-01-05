#T02_21
#кількість дійсних розв’язків рівняння ax**2 + bx + c = 0

from math import sqrt

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
    d = b**2 - 4*a*c
    if d >= 0:
        k=2
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
    else:
        k=0

if k == -1:
    print ('безліч')
elif k == 0:
    print ('немає')
elif k == 1:
    print('x1 = ', x1)
else:
    print('x1 = ', x1)
    print('x2 = ', x2)
    
              
    

