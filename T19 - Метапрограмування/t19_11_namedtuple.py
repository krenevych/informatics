#T19_11
#Реалізація класу named_tuple
#Взято з "Python Cookbook" by David Beazley and Brian K. Jones 

import operator
import types
import sys

def named_tuple(classname, fieldnames):
    '''Функція створює та повертає клас, що реалізує іменований кортеж.

    classname - ім'я створюваного класу,
    fieldnames - послідовність імен полів.
    Функція повертає модифікований клас для реалізації звичайних кортежів (tuple),
    змінюючи в ньому метод __new__
    '''
    
    # Заповнити словник функціями доступу до полів кортежу за їх номерами
    # Ключі у словнику - імена полів іменованого кортежу
    # cls_dict буде містити імена атрибутів нового класу
    # operator.itemgetter(n) - функція, що повертає n-ий елемент послідовності
    cls_dict = { name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames) }

    # Створити нову функцію __new__ та додати до словника класу
    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            #перевірити, чи рівна кількість полів при ініціалізації об'єкта
            #кількості полів у описі класу
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        # викликати та повернути результат __new__ з стандартного класу tuple  
        return tuple.__new__(cls, args) 

    cls_dict['__new__'] = __new__

    # Створити клас за допомогою types.new_class
    cls = types.new_class(classname, (tuple,), {},
                        lambda ns: ns.update(cls_dict))
#У даному випадку можна було використати й функцію type наступним чином:
#    cls = type(classname, (tuple,), cls_dict)

    # встановити ім'я модуля рівним імені модуля, звідки викликається named_tuple
    cls.__module__ = sys._getframe(1).f_globals['__name__'] #ненадійно!
    return cls

