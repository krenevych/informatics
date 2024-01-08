#T18_31
#Використання "домішків" (mixins) та множинне наслідування.
#Взято з "Python Cookbook" by David Beazley and Brian K. Jones

from T16.t16_41_polynome_ex_it import *

class LoggedMappingMixin:
    '''Додати виведення операцій get/set/delete для налагодження.
    '''

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class LoggedPolynome(LoggedMappingMixin, PolynomeEx):
    '''Клас, що успадковує від PolynomeEx та домішку LoggedMappingMixin.
    '''
    pass


if __name__ == '__main__':
    def copy_polynome(p):
        """
        Функція реалізує копіювання поліному за допомогою ітератора
        :param p: поліном
        :return: поліном - копія p
        """
        p1 = LoggedPolynome()
        for coeff, deg in PolynomeIt(p):
            p1.add_monom(deg, coeff)
        return p1

    p = LoggedPolynome.fromstring("1.1*x**0 + -2.3*x**2 + 0.9*x**5")
    for coeff, deg in PolynomeIt(p):
        print("Одночлен. Коефіцієнт {} степінь {}".format(coeff, deg))

    pp = copy_polynome(p)
    print(pp)
