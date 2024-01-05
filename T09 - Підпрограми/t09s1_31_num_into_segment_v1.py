#T09s1_31_v1
#Порахувати кількість компонент вектора, які належать відрізку [a, b].
#Використати функцію для введення вектора.
#За угодою вектор складається з 10 компонент, а відрізок - [0, 1].


def inputvec (n = 10):
    v=[]
    for i in range(n):
        x = float(input('v[{}]='.format(i+1)))
        v.append(x)
    return v    

def numintosegment (v, a = 0, b = 1):
    k = 0
    for x in v:
        if a <= x <= b:
            k = k+1
    return k


#обчислення за угодою

v = inputvec()
m = numintosegment(v)

print('Кількість компонент на відрізку [0,1]=',m) 

#обчислення за заданими параметрами
n=int(input("\nКількість компонент: "))
x1=float(input("Початок відрізку: "))
x2=float(input("Кінець відрізку: "))

v = inputvec(n)
m = numintosegment(v,x1,x2)

print('Кількість компонент на відрізку [{},{}]={}'.format(x1,x2,m))

#Використання ключів при виклику
m = numintosegment(a = x1, b = x2, v = v)
print('Кількість компонент на відрізку (ключі) [{},{}]={}'.format(x1,x2,m))
