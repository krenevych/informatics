#T02_02
#max 3

a = float(input("a=? "))
b = float(input("b=? "))
c = float(input("c=? "))

if a < b:
    max = b
else:
    max = a

if max < c:
    max = c

    
print("max = ", max)
