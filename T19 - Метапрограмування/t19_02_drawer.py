#T19_02

#Абстрактний клас Drawable та клас-нащадок TurtleDraw

from abc import ABCMeta, abstractmethod
import turtle

class Drawable(metaclass = ABCMeta):
    """Абстрактний клас для зображення точок та кіл заданих розмірів та кольору

    """
    @property
    @abstractmethod
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        pass

    @color.setter
    @abstractmethod
    def color(self, cl):
        pass

    @property
    @abstractmethod
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        pass

    @bgcolor.setter
    @abstractmethod
    def bgcolor(self, cl):
        pass

    @abstractmethod
    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        pass

    @abstractmethod
    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цнтру x, y радіусом r кольором cl."""
        pass


            
class TurtleDraw(Drawable):
    """Клас для зображення точок та кіл заданих розмірів та кольору.

    TurtleDraw є нащадком абстрактного класу Drawable та використовує засоби
    роботи з графікою з модуля turtle.
    """
    
    def __init__(self):
        pause = 50
        turtle.up()
        turtle.home()
        turtle.delay(pause)

    @property
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        return turtle.pencolor()

    @color.setter
    def color(self, cl):
        turtle.pencolor(cl)

    @property
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        return turtle.bgcolor()

    @bgcolor.setter
    def bgcolor(self, cl):
        turtle.bgcolor(cl)

    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.dot(cl)

    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цнтру x, y радіусом r кольором cl."""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y-r) #малює починаючи знизу кола
        turtle.down()
        turtle.circle(r)
        self.color = c
     





