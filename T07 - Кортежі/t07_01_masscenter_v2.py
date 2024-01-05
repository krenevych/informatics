#T07_01_v2
#Центр мас системи матеріальних точок простору та найбільша відстань між точками
from math import sqrt
from collections import namedtuple

#Описуємо Point3 як точку з координатами x,y,z
Point3 = namedtuple('Point3d',['x','y','z'])

n=int(input("кількість точок: "))

a=[]                        #a - список точок
for i in range(n):
    print('точка ', i+1)
    #x,y,z - координати точки
    x = float(input('x='))
    y = float(input('y='))
    z = float(input('z='))
    t = Point3(x,y,z)       #t - точка з координатами x,y,z
    a.append(t)

c = Point3(0,0,0)           #c - точка - центр мас
for current in a:
    c = Point3(c.x+current.x, c.y+current.y, c.z+current.z) #рахуємо суму координат
c = Point3(c.x/n, c.y/n, c.z/n)     #ділимо на кількість точок

print('центр мас:',*c)

dmax = 0                #dmax - максимальна відстань між двома точками
for i in range(n):
    for j in range(i+1,n):
        #dij - відстань між точками з номерами i та j
        dij = sqrt((a[i].x-a[j].x)**2 + (a[i].y-a[j].y)**2 + (a[i].z-a[j].z)**2)
        if dij > dmax:
            dmax = dij

print('максимальна відстань:',dmax)    
