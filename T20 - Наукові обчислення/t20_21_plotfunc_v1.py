#T20_21_v1
#Зображення графіку функції f на інтервалі [a,b] у n точках

import numpy as np
import matplotlib.pyplot as plt
from t20_11_tabulate_v3 import *
from math import sin
#from numpy import sin


def plotfunc1(a, b, n, f):
    '''Зображує графік функції f на інтервалі [a,b] у n точках
    '''
    x, y = tabulate(f, a, b, n) #табулювати функцію
    plt.plot(x, y)              #створити графік
    plt.show()                  #показати графік

if __name__ == '__main__':
    n = int(input('Кількість точок: '))
    a = float(input('Початок відрізку: '))
    b = float(input('Кінець відрізку: '))


    funcs = [fun, sin]
    for ff in funcs:
        plotfunc1(a, b, n, ff)
