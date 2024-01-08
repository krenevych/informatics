# t16_42_polynome_ex_gen.py
# Поліном. Генератор

from T15.t15_41_polynome_ex import PolynomeEx


def polynome_gen(polynome):
    """Гененратор для PolynomeEx.

    Генератор повертає усі одночлени поліному у порядку спадання степенів
    """
    cur_degree = polynome.get_degree() + 1
    while True:
        cur_degree -= 1
        if cur_degree < 0:
            break

        if cur_degree in polynome:
            yield polynome[cur_degree], cur_degree

if __name__ == '__main__':
    def copy_polynome(p):
        """
        Функція реалізує копіювання поліному за допомогою генератора
        :param p: поліном
        :return: поліном - копія p
        """
        p1 = PolynomeEx()
        for coeff, deg in polynome_gen(p):
            p1.add_monom(deg, coeff)
        return p1

    p = PolynomeEx.fromstring("1.1*x**0 + -2.3*x**2 + 0.9*x**5")
    for coeff, deg in polynome_gen(p):
        print("Одночлен. Коефіцієнт {} степінь {}".format(coeff, deg))

    pp = copy_polynome(p)
    print(pp)
