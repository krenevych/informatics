#T19_21
#Опис та використання метакласів
#Реалізація метакласу StructTupleMeta та класу StructTuple
#Взято з "Python Cookbook" by David Beazley and Brian K. Jones 

import operator

class StructTupleMeta(type):
    '''Метаклас, що створює клас, подібний структурі C.

    Метаклас доповнює словник створюваного класу властивостями
    з іменами, що містяться у списку _fields.
    Для читання значення кожної властивості використовується
    operator.itemgetter(n) - отримання n-го елементу послідовності
    '''
    def __init__(cls, name, bases, nmspc):
        """Конструктор __init__ метакласу.

        Приймає параметри для створення класу (не об'єкту!).
        cls - клас, name - його ім'я,
        bases - кортеж з базових класів, nmspc - словник класу
        """
#        print('meta _init_', cls, name, bases, nmspc, cls._fields, sep = '\n')
        #Виклик конструктора базового класу
        super().__init__(name, bases, nmspc)
        for n, name in enumerate(cls._fields):
            #додати у клас властивість з ім'ям name
            #та методом читання operator.itemgetter(n)
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    '''Клас, подібний структурі C.

    Модифікує __new__ для перевірки рівності кількості полів та параметрів
    '''
    _fields = []    #список імен полів

    def __new__(cls, *args):
#        print('__new__', cls, args, cls._fields)
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return tuple.__new__(cls, args) #виклик tuple.__new__ для створення кортежу


