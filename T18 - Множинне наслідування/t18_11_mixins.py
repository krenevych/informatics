#T18_11
#Використання "домішків" (mixins) та множинне наслідування.
#Граф з логуванням
#Взято з "Python Cookbook" by David Beazley and Brian K. Jones

from T16.t16_21_graphit import *
from T16.t16_22_istree import *

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


class LoggedGraph(LoggedMappingMixin, GraphIt):
    '''Клас, що успадковує від GraphIt та домішку LoggedMappingMixin.
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

