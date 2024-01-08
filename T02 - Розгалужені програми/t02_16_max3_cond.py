# t02_16_max3.py
# Обчислання max{a,b,c} за допомогою умовного виразу

a = float(input('a=?'))
b = float(input('b=?'))
c = float(input('c=?'))

max = a if a >= b else b
max = c if max < c else max

print ('max= ', max)
