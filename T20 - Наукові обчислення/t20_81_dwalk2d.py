#T20_81
#Випадковий шлях у двовимірному просторі ("хода п'яниці")
#Змоделювати заповнення визначеного об'єму молекулами газу

import numpy as np
import matplotlib.pyplot as plt

class Drunkard2D:
    '''Клас, що реалізує випадковий шлях у двовимірному просторі ("хода п'яниці").

    
    '''
    def __init__(self, num_drunkards, init_pos = None, is_limited = False, bounds = None):
        self._n_d = num_drunkards           #кількість точок
        self._is_limited = is_limited       #чи обмежена область
        self._bounds = bounds               #границі області (прямокутник)

        self._pos = init_pos                #позиції всіх точок
        if self._pos is None:
            #якщо позиції не задано, встановлюємо всі у (0,0)
            self._pos = np.zeros(self._n_d * 2)
            self._pos.shape = (2, self._n_d)
            if self._is_limited:
                #якщо задано границі, встановлюємо всі точки у середину області
                xmin, ymin, xmax, ymax = self._bounds
                x = (xmin + xmax) // 2
                y = (ymin + ymax) // 2
                self._pos += np.array([[x], [y]])
                
        self._dirs = np.array([[-1, 0], [0, -1], [1, 0], [0, 1]]) #можливі рухи
        self._dirs = np.transpose(self._dirs) #зручніше мати транспонований масив

        self.fig_count = 0  #номер рисунку

        plt.hold(False)     #кожного разу буде малювати нове зображення,
                            #а не доповнювати попереднє


    @property
    def bounds(self):
        '''Властивість границі (читання).'''
        return self._bounds

    @bounds.setter
    def bounds(self, new_bounds):
        '''Властивість границі (встановлення).'''
        self._bounds = new_bounds

    @property
    def pos(self):
        '''Властивість позиції точок (тільки читання).'''
        return self._pos

    def _push_into_bounds(self):
        '''Повернути всі точки у межі області.'''
        xmin, ymin, xmax, ymax = self._bounds
        self.pos[0][self.pos[0] < xmin] = xmin + 1
        self.pos[0][self.pos[0] > xmax] = xmax - 1
        self.pos[1][self.pos[1] < ymin] = ymin + 1
        self.pos[1][self.pos[1] > ymax] = ymax - 1

    def step(self):
        '''Зробити один крок у моделюванні.'''
        #масив індексів для подальшого формування масиву приростів
        ids = np.random.random_integers(0, 3, self._n_d)
#        print(ids)
#        print(self._dirs)

        #масив приростів чергового кроку
        dxy = self._dirs[:,ids]
#        print(dxy)
        self._pos += dxy
        if self._is_limited:
            self._push_into_bounds()
        
    def msteps(self, m):
        '''Зробити m кроків у моделюванні.'''
        for i in range(m):
            self.step()
        
    def plot(self):
        '''Побудувати графік стану моделі.'''
        #set axes
        if self._bounds is None:
            xmin = ymin = -100
            xmax = ymax = 100
        else:
            xmin, ymin, xmax, ymax = self._bounds
        plt.plot(self._pos[0], self._pos[1], 'ob')
        plt.axis([xmin, xmax, ymin, ymax])

    def show(self):
        '''Побудувати та показати графік стану моделі.'''
        self.plot()
        plt.show()
            
        
    def savefig(self, path):
        '''Побудувати та зберегти графік стану моделі у файлі.

        path - шлях до файлу, включаючи фінальний символ
        поділу каталогів ('/' або '\').
        Файл має ім'я відповідно масці
        tmpXXXXX.png, деXXXXX - номер рисунку 
        '''
        self.fig_count += 1
        fname = "tmp{:0>5}.png".format(self.fig_count)
        self.plot()
        plt.savefig(path + fname)
        


if __name__ == '__main__':
    ds = Drunkard2D(1000)
    ds.msteps(2000)
    ds.show()

