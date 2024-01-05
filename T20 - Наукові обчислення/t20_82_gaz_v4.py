#T20_82_v3
#Змоделювати заповнення визначеного об'єму молекулами газу
#Створити анімацію зі збережених файлів зображень у matplotlib


import numpy as np
import matplotlib.pyplot as plt
from t20_81_dwalk2d import *
from matplotlib import animation

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

#Побудова, запуск та збереження анімації

plt.hold(True)      #встановити зображення декількох графіків
                    
fig = plt.figure()                          #створити нове вікно
xmin, ymin, xmax, ymax = ds.bounds
ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax)) #задати осі
line, = ax.plot([], [], 'ob', lw=2)     #повернути об'єкт для подальшої анімації

def init():
    """Очистити поточний кадр."""
    line.set_data([], [])               #повернути порожній графік
    return line,

def animate(i):
    """Зобразити рисунок.
    @param i: Лічильник кадрів
    @type i: int
    """
    ds.msteps(m)                        #виконати m кроків
    line.set_data(ds.pos[0], ds.pos[1]) #передати дані (x, y) для наступного кадру
    return line,


# Цей виклик запускає анімацію
# зв'язує функції init та animate а також рисунок
animator = animation.FuncAnimation(fig, animate, init_func=init, 
                frames=steps_num//m, interval=40, repeat=False)
plt.show()


