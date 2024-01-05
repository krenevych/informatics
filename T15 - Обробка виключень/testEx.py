
import random, logging



y = float(input("Enter num "))
try:
    x = float(input("Enter num "))
    assert x != 0, "Assertion: Div by zero"
except AssertionError as a:
    print(a)
  #  logging.error(a.msg)
else:
    print ('y/x = ', y/x)
    
