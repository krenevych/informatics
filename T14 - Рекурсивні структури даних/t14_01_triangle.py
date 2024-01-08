# Класи Точка, Відрізок та Трикутник
from math import sqrt

class Point2:
    """Клас реалізує точку площини"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        """Повернути координату х"""
        return self._x

    def get_y(self):
        """Повернути координату y"""
        return self._y

    def __str__(self):
        """Повернути рядок представлення точки"""
        return "({}, {})".format(self._x, self._y)


class Segment:
    """Клас реалізує відрізок на площині"""

    def __init__(self, a, b):
        self._a = a     # точка
        self._b = b     # точка

    def get_a(self):
        """Повернути точку a"""
        return self._a

    def get_b(self):
        """Повернути точку b"""
        return self._b

    def __str__(self):
        """Повернути рядок представлення відрізку"""
        return "[{}, {}]".format(self._a, self._b)

    def len(self):
        return sqrt((self._a.get_x() - self._b.get_x()) ** 2 +
                    (self._a.get_y() - self._b.get_y()) ** 2)

class Triangle:
    """Клас реалізує трикутник"""

    def __init__(self, a, b, c):
        self._a = a     # точка
        self._b = b     # точка
        self._c = c     # точка

    def get_a(self):
        """Повернути точку a"""
        return self._a

    def get_b(self):
        """Повернути точку b"""
        return self._b

    def get_c(self):
        """Повернути точку c"""
        return self._c

    def __str__(self):
        """Повернути рядок представлення трикутника"""
        return "Трикутник ({}, {}, {})".format(self._a, self._b, self._c)

    def _get_sides(self):
        s1 = Segment(self._a, self._b).len()
        s2 = Segment(self._b, self._c).len()
        s3 = Segment(self._a, self._c).len()
        return s1, s2, s3

    def perimeter(self):
        """Повернути периметр трикутника"""
        s1, s2, s3 = self._get_sides()
        return s1 + s2 + s3

    def square(self):
        p = self.perimeter() / 2
        s1, s2, s3 = self._get_sides()
        return sqrt(p * (p - s1) * (p - s2) * (p - s3))
