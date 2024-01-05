#T04_11_v1
#Обчислення sin(x) з уникненням переповнення

x = float(input('введіть x: '))
eps = float(input('введіть eps: '))

z = x
y = x
k = 0
while abs(z) >= eps:
    k = k+1
    z = -z*x*x/(2*k*(2*k+1))
    y += z

print ('Результат ',y)
