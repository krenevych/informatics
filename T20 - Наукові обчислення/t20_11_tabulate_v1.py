#T20_11_v1
#Табулювання функції f на інтервалі [a,b] у n точках

import numpy as np
from math import sin


def gety(f, x):
    '''Повертає значення функції f для всіх точок з x
    '''
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y



def tabulate(f, a, b, n):
    '''Табулює функцію f на інтервалі [a,b] у n точках
    '''
    x = np.linspace(a, b, n)
    y = gety(f, x)
    return x, y


def fun(x):
    '''Обчислює x**3 - 7*x - 1
    '''
    return x**3 - 7*x - 1

if __name__ == '__main__':
    n = int(input('Кількість точок: '))
    a = float(input('Початок відрізку: '))
    b = float(input('Кінець відрізку: '))


    funcs = [fun, sin]
    for ff in funcs:
        x, y = tabulate(ff, a, b, n)
        if n < 50:
            print('\n', x, '\n', y)
        print('Зроблено для', ff.__name__)

