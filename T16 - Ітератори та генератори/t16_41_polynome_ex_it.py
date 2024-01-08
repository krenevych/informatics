# t16_41_polynome_ex_it.py
# Поліном. Ітератор

from T15.t15_41_polynome_ex import PolynomeEx


class PolynomeIt:
    """Даний клас реалізує ітератор для PolynomeEx.

    Ітератор повертає усі одночлени поліному у порядку спадання степенів
    """
    def __init__(self, polynome):
        self._polynome = polynome
        self._cur_degree = self._polynome.get_degree() + 1

    def __iter__(self):
        return self

    def __next__(self):
        """
        Повертає наступний одночлен поліному в порядку спадання степенів.
        """
        while True:
            self._cur_degree -= 1
            if self._cur_degree < 0:
                raise StopIteration

            if self._cur_degree in self._polynome:
                break

        return self._polynome[self._cur_degree], self._cur_degree

if __name__ == '__main__':
    def copy_polynome(p):
        """
        Функція реалізує копіювання поліному за допомогою ітератора
        :param p: поліном
        :return: поліном - копія p
        """
        p1 = PolynomeEx()
        for coeff, deg in PolynomeIt(p):
            p1.add_monom(deg, coeff)
        return p1

    p = PolynomeEx.fromstring("1.1*x**0 + -2.3*x**2 + 0.9*x**5")
    for coeff, deg in PolynomeIt(p):
        print("Одночлен. Коефіцієнт {} степінь {}".format(coeff, deg))

    pp = copy_polynome(p)
    print(pp)
