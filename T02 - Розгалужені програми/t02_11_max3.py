#T02_11
#max{a,b,c}

a = float(input('a=?'))
b = float(input('b=?'))
c = float(input('c=?'))
if a > b:
    max = a
else:
    max = b

if max > c:
    c=max

print ('max= ',c)
