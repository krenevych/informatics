#T20_21_v4
#Зображення графіку декількох функцій на інтервалі [a,b] у n точках
#Встановлення осей, легенди, способу зображення, кольору ліній
#Використання subplot

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

def movespinesticks():
    '''Перемістити осі у нульову позицію
    '''
    ax = plt.gca()  #отримати поточний об'єкт класу axes
    # зробити праву та верхню осі невидимими:
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # перенести нижню вісь у позицію y=0:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    # перенести ліву вісь у позицію x == 0:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    

def plotfunc4(a, b, n, *f):
    '''Зображує графік функцій *f на інтервалі [a,b] у n точках
    '''
    tabb = False    #чи було табульовано першу функцію
    m = len(f)      #кількість функцій
    for i,ff in enumerate(f):
        style = styles[i % len(styles)] + colors[i % len(colors)]
#        style = np.random.choice(styles) + np.random.choice(colors)
        if not tabb:
            x, y = tabulate(ff, a, b, n)    #табулювати функцію
            plt.subplot(m, 1, 1)            #перший підграфік
            tabb = True
        else:
            y = gety(ff, x)                 #отримати y за x для функції
            plt.subplot(m, 1, i + 1)        #черговий підграфік
        movespinesticks()               #перемістити осі
        plt.xlabel('x')                 #встановити надпис на осі x
        plt.ylabel('y')                 #встановити надпис на осі y
        plt.plot(x, y, style, label = ff.__doc__) #створити графік з легендою
        plt.legend(loc = 'best')          #встановити легенду
    plt.show()                      #показати графік

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
    plotfunc4(a, b, n, *funcs)
