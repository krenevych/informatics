#T20_82_v1
#Змоделювати заповнення визначеного об'єму молекулами газу

import numpy as np
import matplotlib.pyplot as plt
from t20_81_dwalk2d import *

nd = int(input('Кількість молекул: '))
steps_num = int(input('Загальна кількість кроків: '))
print('Розмір області')
a = int(input('Довжина: '))
b = int(input('Ширина: '))
x1 = int(input('Довжина початкової області: '))

m = 100 # кількість кроків між показами результату

# Завдання початкового розташування молекул у прямокутнику, обмеженому x1
x = np.random.random_integers(0, x1, nd)
y = np.random.random_integers(0, b, nd)
xy = np.vstack((x, y))

# Створення об'єкту класу Drunkard2D 
ds = Drunkard2D(nd, xy, True, (0, 0, a, b))

ds.show()                           #показати стан моделі

for i in range(0, steps_num, m):
    ds.msteps(m)                    #зробити m кроків        
    ds.show()                       #показати стан моделі
    ds.savefig('tmp\\')             #побудувати та зберегти зображення

