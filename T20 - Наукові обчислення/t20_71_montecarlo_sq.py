#T20_71
#Обчислення площ фігур методом Монте-Карло
#Обчислити площу між кривими
# exp(1/x) та a*x**2 + b*x + c

import numpy as np
import matplotlib.pyplot as plt
import operator
from t20_11_tabulate_v3 import *


TEST_NUM = 100000


def trinomial(a, b, c):
    '''Повертає функцію t, що обчислює a*x**2 + b*x + c.'''
    def t(x):
        '''a*x**2 + b*x + c.'''
        return a*x**2 + b*x + c
    return t

def exp1x(x):
    '''exp(1/x).'''
    return np.exp(1/x)


def get_box_bounds(a, b, c):
    '''Обчислює границі прямокутника, у якому повністю розміщено нашу фігуру.'''
    if a >= 0:
        raise ValueError('a = {}. Повинно бути a < 0'.format(a))
    xmin = 2.0e-1               #exp(1/x) дає помилку у 0
    ymin = 0
    ymax = c - b**2/(4*a)+1
    if ymax < 0:                #якщо верхня точка параболи нижче осі абсцис
        ymax = ymin             #зробити порожній прямокутник, перетину не буде
        xmax = xmin
    else:
        xmax = (-b - np.sqrt(b**2 - 4*a*c))/(2*a) + 1
    return xmin, xmax, ymin, ymax

def mc_square(f1, f2, xmin, xmax, ymin, ymax):
    '''Обчислює площу між функціями f1 та f2 методом Монте-Карло.

    xmin, xmax, ymin, ymax - границі прямокутника,
    у якому повністю розміщено нашу фігуру.'''

#    print(xmin, xmax, ymin, ymax)

    x = np.random.uniform(xmin, xmax, TEST_NUM) #масив координат x
#    print(x)

    y = np.random.uniform(ymin, ymax, TEST_NUM) #масив координат y
    y1 = f1(x)                                  #масив значень функції f1
#    print(y1)
    y2 = f2(x)                                  #масив значень функції f2
#    print(y2)

    count_in = len(y[np.logical_and(y1 <= y, y <= y2)]) #кількість точок,
                                                        #що потрапили в область
    s = count_in / TEST_NUM * ((xmax - xmin) * (ymax - ymin)) #площа

    return s
    

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

    

def plotf1f2(a, b, c, d, n, f1, f2):
    '''Зображує графік функцій f1, f2 на інтервалі [a,b] у n точках

    c, d - ординати прямокутника, що охоплює графіки функцій.
    Область між f1 та f2 заливається кольором.
    Також зображує пунктиром прямокутник [(a,c),(b,d)]
    '''
    x, y1 = tabulate(f1, a, b, n)   #табулювати функцію f1
    plt.plot(x, y1)                 #створити графік

    y2 = gety(f2, x)                #отримати y2 за x для функції f2

    #заповнити область, в якій наступна функція більше попередньої
    plt.fill_between(x, y1, y2, where = y1 <= y2, facecolor = 'cyan')
    plt.plot(x, y2)                 #створити графік

    movespinesticks()               #перемістити осі
    plt.xlabel('x')                 #встановити надпис на осі x
    plt.ylabel('y')                 #встановити надпис на осі y
    #зобразити охоплюючий прямокутник
    plt.plot([a, a], [c, d], '--k')
    plt.plot([b, b], [c, d], '--k')
    plt.plot([a, b], [c, c], '--k')
    plt.plot([a, b], [d, d], '--k')
    
    plt.show()                      #показати графік



if __name__ == '__main__':
    a = float(input('a (<0) = '))
    b = float(input('b = '))
    c = float(input('c = '))
    
    xmin, xmax, ymin, ymax = get_box_bounds(a, b, c)
#    print(xmin, xmax, ymin, ymax)
    tri = trinomial(a, b, c)

    s = mc_square(exp1x, tri, xmin, xmax, ymin, ymax)
    print('Площа між кривими', s)
    plotf1f2(xmin, xmax, ymin, ymax, 1000, exp1x, tri)
    

