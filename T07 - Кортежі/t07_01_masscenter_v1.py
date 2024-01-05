#T07_01_v1
#Центр мас системи матеріальних точок простору та найбільша відстань між точками
from math import sqrt

n=int(input("кількість точок: "))

a=[]                    #a - список точок
for i in range(n):
    print('точка ', i+1)
    #x,y,z - координати точки
    x = float(input('x='))
    y = float(input('y='))
    z = float(input('z='))
    t = (x,y,z)         #t - точка з координатами x,y,z
    a.append(t)

c = (0,0,0)             #c - точка - центр мас
for i in range(n):
    c = (c[0] + a[i][0], c[1] + a[i][1], c[2] + a[i][2])    #рахуємо суму координат
c = (c[0]/n, c[1]/n,c[2]/n) #ділимо на кількість точок

print('центр мас:',c)

dmax = 0                #dmax - максимальна відстань між двома точками
for i in range(n):
    for j in range(i+1,n):
        #dij - відстань між точками з номерами i та j
        dij = sqrt((a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2 + (a[i][2]-a[j][2])**2)
        if dij > dmax:
            dmax = dij

print('максимальна відстань:',dmax)    
