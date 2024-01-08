#T19_05
#Декоратори класів.
#Граф з логуванням

from T16.t16_21_graphit import *
from T16.t16_22_istree import *

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
class LoggedGraph(GraphIt):
    '''Клас, що успадковує від GraphIt.

    Застосовується декоратор logged_mapping
    '''
    pass


if __name__ == '__main__':
    filename = input("Введіть ім'я файлу: ")
    g = LoggedGraph()
    fileinputgraph(filename, g)
    if istree(g):
        print("Граф є деревом")
    else:
        print("Граф не є деревом")

