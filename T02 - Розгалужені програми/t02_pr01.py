#T02_02
#max 3

import math

x = float(input("x=? "))
y = float(input("y=? "))

if ( (x*x + y*y <= 4 and x <= 0) or
    math.fabs(x) + math.fabs(y) <= 2 and x > 0):
    print("result = True")
else:
    print ("result = False")
