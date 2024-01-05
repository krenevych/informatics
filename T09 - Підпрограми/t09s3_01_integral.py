#T09s3_01
#Визначити значення інтегралу функції на відрізку [a, b].
from math import sin

def integral(f, a = 0, b = 1, eps = 10e-7):
    '''Обчислює значення інтегралу функції f на відрізку [a, b].

    Значення обчислюється наближено поки модуль різниці
    між двома послідовними наближеннями не стане менше за eps.
    '''
    n = 1
    h = b-a
    s = (f(a)+f(b))*h/2
    while True:
        n *= 2
        h = (b-a)/n
        s1 = s
        s = 0
        y = f(a)
        for i in range(n):
            x = a+(i+1)*h
            y1 = y
            y = f(x)
            s += (y1+y)*h/2
        if abs(s-s1) < eps: break
    return s

def fun(x):
    '''x**3-7*x+1.

    '''
    return x**3-7*x+1

a = float(input("Початок відрізку: "))
b = float(input("Кінець відрізку: "))

m = integral(fun,a,b)
print('Інтеграл функції {}\n на відрізку [{},{}]={}'.format(fun.__doc__ ,a,b,m))

m = integral(sin,a,b)
print('Інтеграл функції {}\n на відрізку [{},{}]={}'.format(sin.__doc__ ,a,b,m))

