#T07_08_v1
#Транспонування матриці з використанням функції zip

m=int(input("кількість рядків: "))
n=int(input("кількість стовпчиків: "))
#введення матриці a
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        x = float(input('a[{},{}]='.format(i+1,j+1)))
        a[i].append(x)

#виведення матриці a
print('\nМатриця')
for i in range(m):
    print(a[i])

#отримання транспонованої матриці t
t = list(zip(*a))

#виведення транспонованої матриці t
print('\nТранспонована матриця')
for i in range(n):
    print(t[i])


