#T13_11_v2
#Зв'язування об'єктів та методів, віртуальні методи
#Точки та кола

import turtle

class Point:
    '''Точка екрану

    '''
    _count = 0

    def __init__(self, x, y):
        self._x = x             # _x - координата x точки
        self._y = y             # _y - координата y точки
        self._visible = False   # _visible - чи є точка видимою на екрані
        Point._count += 1

    def getx(self):
        '''Повертає координату x точки
        '''
        return self._x

    def gety(self):
        '''Повертає координату y точки
        '''
        return self._y

    def onscreen(self):
        '''Перевіряє, чи є точка видимою на екрані
        '''
        return self._visible

    def switchon(self):
        '''Робить точку видимою на екрані
        '''
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot()

    def switchoff(self):
        '''Робить точку невидимою на екрані
        '''
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(turtle.bgcolor())

    def move(self, dx, dy):
        '''Пересуває точку на екрані на dx, dy позицій
        '''
        vis = self._visible
        if vis:
            self.switchoff()
        self._x += dx
        self._y += dy
        if vis:
            self.switchon()
            
    def printcount():
        print('Кількість точок:', Point._count)

    printcount = staticmethod(printcount)


class Circle(Point):
    '''Коло на екрані

    '''
    _count = 0

    def __init__(self, x, y, r):
        Point.__init__(self, x, y)
        self._r = r                 # _r - радіус кола 
        Circle._count += 1
        Point._count -= 1           #Point.__init__ збільшує Point._count на 1

    def getr(self):
        '''Повертає радіус кола
        '''
        return self._r

    def switchon(self):
        '''Робить коло видимим на екрані
        '''
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y-self._r) #малює починаючи знизу кола
            turtle.down()
            turtle.circle(self._r)

    def switchoff(self):
        '''Робить коло невидимим на екрані
        '''
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y-self._r) #малює починаючи знизу кола
            turtle.down()
            c = turtle.pencolor()
            turtle.pencolor(turtle.bgcolor())
            turtle.circle(self._r)
            turtle.pencolor(c)

    def printcount():
        print('Кількість кіл:', Circle._count)

    printcount = staticmethod(printcount)

#Завершено опис та реалізацію класів
if __name__ == '__main__':
    pause = 50
    turtle.home()
    turtle.delay(pause)
    p = Point(50,50)
    p.switchon()
    p.move(-100,20)
    c = Circle(120,120,30)
    c.switchon()
    c.move(-30,-140)



