#T06_01
#Обчислення скалярного добутку 2 векторів

n=int(input("кількість компонент: "))

#введення 1 вектору
a=[]
for i in range(n):
    x = float(input('a['+str(i+1)+']='))
    a.append(x)
#введення 2 вектору
b=[]
for i in range(n):
    x = float(input('b['+str(i+1)+']='))
    b.append(x)
#обчислення скалярного добутку
s=0
for i in range(n):
    s += a[i]*b[i]

print('s=',s)



