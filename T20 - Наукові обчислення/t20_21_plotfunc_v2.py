#T20_21_v2
#Зображення графіку декількох функцій на інтервалі [a,b] у n точках

import numpy as np
import matplotlib.pyplot as plt
from t20_11_tabulate_v3 import *
from math import sin
#from numpy import sin


def plotfunc2(a, b, n, *f):
    '''Зображує графік функцій *f на інтервалі [a,b] у n точках
    '''
    tabb = False            #чи було табульовано першу функцію
    for ff in f:
        if not tabb:
            x, y = tabulate(ff, a, b, n) #табулювати функцію
            tabb = True
        else:
            y = gety(ff, x)             #отримати y за x для функції
        plt.plot(x, y)              #створити графік
    plt.show()              #показати графік

def sindivx(x):
    '''sin(x)/x
    '''
    if x == 0:
        return 1
    else:
        return sin(x)/x

if __name__ == '__main__':
    n = int(input('Кількість точок: '))
    a = float(input('Початок відрізку: '))
    b = float(input('Кінець відрізку: '))


    funcs = [fun, sindivx]
    plotfunc2(a, b, n, *funcs)
