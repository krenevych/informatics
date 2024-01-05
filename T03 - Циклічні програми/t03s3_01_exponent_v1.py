#Обчислення експоненти
x = float(input('введіть x: '))
eps = float(input('введіть eps: '))
y = 1
z = 1
k = 0

while abs(z) >= eps:
    k = k+1
    z = z*x/k
    y = y+z

print ('Результат',y)
