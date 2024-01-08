#T19_05
#Декоратори класів.
#Граф з логуванням

from T16.t16_41_polynome_ex_it import *

def logged_mapping(cls):
    '''Додати виведення операцій get/set/delete для налагодження.
    '''
    #Отримати наявні у класі методи __getitem__, __setitem__, __delitem__
    orig_getitem = cls.__getitem__
    orig_setitem = cls.__setitem__
    orig_delitem = cls.__delitem__
    
    def log_getitem(self, key):
        print('Getting ' + str(key))
        return orig_getitem(self, key)

    def log_setitem(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return orig_setitem(self, key, value)

    def log_delitem(self, key):
        print('Deleting ' + str(key))
        return orig_delitem(self, key)

    #Зберегти у класі модифіковані методи __getitem__, __setitem__, __delitem__
    cls.__getitem__ = log_getitem 
    cls.__setitem__ = log_setitem 
    cls.__delitem__ = log_delitem
    return cls


@logged_mapping
class LoggedPolynome(PolynomeEx):
    '''Клас, що успадковує від PolynomeEx.

    Застосовується декоратор logged_mapping
    '''
    pass


if __name__ == '__main__':
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

