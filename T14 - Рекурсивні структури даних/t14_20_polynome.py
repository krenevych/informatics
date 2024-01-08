#t14_20_polynome.py
#Модуль реалізації кдасу обробки поліномів
from collections import defaultdict


class Polynome(defaultdict):
    """Даний клас реалізує дії над поліномами.

    Поліном представлений у вигляді словника.
    Степінь - ключ, коефіцієнт - значення.
    Зберігаються тільки степені з ненульовими коефіцієнтами.

    Методи:
    input() -> Polynome - Введення поліному з клавіатури.
    fromstring(s) -> Polynome - Перетворення рядка у поліном.
        Рядок повинен мати вигляд (наприклад):
        3.7*x**3 + 0.3*x**1 + -1.2*x**0
    __str__() - Повернути поліном у вигляді рядка.
        Рядок буде мати вигляд (наприклад):
        3.7*x**3 + 0.3*x**1 + -1.2*x**0
    __call__(x) -> float - Значення поліному у точці x.
    __add__(other) -> Polynome - Сума поліномів self + other.
    __radd__(other) -> Polynome - Сума поліномів other + self.
    __sub__(other) -> dict - Різниця поліномів self - other.
    __rsub__(other) -> dict - Різниця поліномів other - self.
    __mul__(other) -> Polynome - Добуток поліномів self * other.
    __rmul__(other) -> Polynome - Добуток поліномів other * self.
    deriv(n = 1) -> dict - n-та похідна поліному self.
    add_monom(deg, coeff) -> None - Додати одночлен
    get_degree() -> int - Повернути степінь поліному
    """

    def __init__(self, **kwargs):
        defaultdict.__init__(self, float, **kwargs)

    def fromstring(s):
        """
        Перетворення рядка у поліном.

        Рядок повинен мати вигляд (наприклад):

        3.7*x**3 + 0.3*x**1 + -1.2*x**0

        Пробіли між коефіцієнтами та степенями не допускаються.
        Від'ємні коефіцієнти записувати як у прикладі вище.
        :param s: рядок
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        s = s.replace('+',' ')
        ls = s.split()  #розбиваємо на список одночленів
        for m in ls:
            c = m.split('*x**') #виділяємо степінь та коефіцієнт
            k = int(c[1])
            v = float(c[0])
            p[k] = v
        return p

    fromstring = staticmethod(fromstring)

    def add_monom(self, deg, coeff):
        """
        Додати одночлен степені deg до поліному.
        :param deg: степінь одночлена
        :param coeff: коефіцієнт одночлена
        :return: None
        """
        if coeff != 0:
            self[deg] += coeff

    def get_degree(self):
        """
        Метод повертає степінь поліному
        :return: степінь полінома (int)
        """
        return max(self)

    def __str__(self):
        """
        Повернути рядок, який є зовнішнім представленням поліному.

        Рядок буде мати вигляд (наприклад):
        3.7*x**3 + 0.3*x**1 + -1.2*x**0
        :return: рядок
        """
        monomials = list(self.items())
        if not monomials:
            poly_str = "0.0*x**0"
        else:
            # Впорядковуємо за спаданням степенів
            monomials.sort(reverse=True)
            ls = ["{}*x**{}".format(mono[1], mono[0]) for mono in monomials]
            poly_str = ' + '.join(ls)
        return poly_str

    def __call__(self, x):
        """
        Значення поліному у точці x.

        :param x: дійсне число
        :return: значення поліному у точці x (дійсне)
        """
        return sum([self[k]*x**k for k in self])

    def __add__(self, other):
        """
        Сума поліномів self + other.
        :param other: поліном
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        # утворюємо множину, що містить всі ключі self та other
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] + other[k]
        return self._delzeroes(p)

    def __radd__(self, other):
        """
        Сума поліномів other + self.
        :param other:
        :return: об'єкт класу Polynome
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Різниця поліномів self - other.
        :param other: поліном
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] - other[k]
        return self._delzeroes(p)

    def __rsub__(self, other):
        """
        Різниця поліномів other - self.
        :param other: поліном
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = other[k] - self[k]
        return self._delzeroes(p)

    def __mul__(self, other):
        """
        Добуток поліномів self * other.
        :param other: поліном
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        for k1 in self:
            for k2 in other:
                p[k1 + k2] += self[k1] * other[k2]
        return self._delzeroes(p)

    def __rmul__(self, other):
        """
        Добуток поліномів other * self.
        :param other: поліном
        :return: об'єкт класу Polynome
        """
        return self.__rmul__(other)

    def deriv(self, n=1):
        """
        n-та похідна поліному self.

        Якщо n не вказано, то перша похідна
        :param n: порядок похідної
        :return: об'єкт класу Polynome
        """
        p = self
        for i in range(n):
            p = self._deriv(p)
        return self._delzeroes(p)

    def _deriv(self, p):
        """
        Перша похідна поліному p.

        :return: об'єкт класу Polynome
        """
        pp = Polynome()
        for k in p:
            if k != 0:
                pp[k - 1] = p[k] * k
        return pp

    def _delzeroes(self, p):
        """
        Повертає копію p без нульових елементів.

        Якщо всі нулі, то повертає поліном 0*x**0.
        :param p: об'єкт класу Polynome
        :return: об'єкт класу Polynome
        """
        pp = Polynome()
        for k in p:
            if p[k] != 0:
                pp[k] = p[k]
        return pp


if __name__ == '__main__':
    p1 = Polynome.fromstring('3.7*x**3 + 0.3*x**1 + -1.2*x**0')
    print('р1 =', p1)
    p2 = Polynome.fromstring('2.2*x**3 + -1.3*x**2 + 0.2*x**1')
    print('р2 =', p2)
    print('Значення p1 у точці x=2:', p1(2))
    print('Сума p1+p2:', p1 + p2)
    print('Різниця p1-p2:', p1 - p2)
    print('Добуток p1*p2:', p1 * p2)
    p = p1.deriv(2)
    print('2 похідна р1:', p)
