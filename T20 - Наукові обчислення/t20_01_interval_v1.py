#T120_01_v1
#Обчислення інтервалу значень вектору (для списків та масивів numpy)

import numpy as np
import random

def interval(x):
    '''Повертає різницю між максимальним та мінімальним елементом списку
    '''
    return max(x) - min(x)

def np_interval(a):
    '''Повертає різницю між максимальним та мінімальним елементом масиву numpy
    '''
    return np.max(a) - np.min(a)



n = int(input('Кількість елементів: '))

x = [random.random() for i in range(n)]
print('створено список')
print('інтервал', interval(x))

a = np.array(x)
print('створено масив numpy')
print('numpy - інтервал', np_interval(a))

