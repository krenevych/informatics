#T20_21_v3
#Зображення графіку декількох функцій на інтервалі [a,b] у n точках
#Встановлення осей, легенди, способу зображення, кольору ліній

import numpy as np
import matplotlib.pyplot as plt
from t20_11_tabulate_v3 import *
from math import sin
#from numpy import sin

#стилі ліній
styles = ['-','--','-.',':','.',',',
          'o','v','^','<','>',
          '1','2','3','4',
          's','p','*','h','H',
          '+','x','D','d','|','_']

#кольори ліній
colors = ['b','g','r','c','m','y','k','w']

def plotfunc3(a, b, n, *f):
    '''Зображує графік функцій *f на інтервалі [a,b] у n точках
    '''
    tabb = False    #чи було табульовано першу функцію
    legend = []     #список рядків легенди
    for i,ff in enumerate(f):
        style = styles[i % len(styles)] + colors[i % len(colors)]
#        style = np.random.choice(styles) + np.random.choice(colors)
        if not tabb:
            x, y = tabulate(ff, a, b, n)    #табулювати функцію
            tabb = True
        else:
            y = gety(ff, x)                 #отримати y за x для функції
        plt.plot(x, y, style)           #створити графік
        legend.append(ff.__doc__)       #додати елемент легенди
    plt.xlabel('x')                 #встановити надпис на осі x
    plt.ylabel('y')                 #встановити надпис на осі y
    plt.legend(legend)              #встановити легенду
    plt.show()                      #показати графік

def sindivx(x):
    '''sin(x)/x !!!!!!!!!!!!!!!!!!!!
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
    plt.title('2 functions')                #встановити заголовок графіку
    plt.axis([0,7,-2,2])                    #встановити осі
    plotfunc3(a, b, n, *funcs)
