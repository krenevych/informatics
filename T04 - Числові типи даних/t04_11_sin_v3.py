#T04_11_v3
#Обчислення sin(x) з уникненням переповнення


from math import pi

x = float(input('введіть x: '))
eps = float(input('введіть eps: '))

m = 1
if x < 0:
    x = -x
    m = -m
x = x%(2*pi)
if x >= pi:
    x = x-pi
    m = -m
if x >= pi/2:
    x = pi-x

#Якщо переведення у інтервал від 0 до pi/2 не робити, то навіть без переповнення
#для не дуже великих х працювати не буде. Можна спробувати х==50.

z = x
y = x
k = 0
while abs(z) >= eps:
    k = k+1
    z = -z*x*x/(2*k*(2*k+1))
    y += z

y = y*m    
print ('Результат ',y)
