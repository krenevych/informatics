#T16_21
#Граф з ітертатором

from T14.t14s3_11_graph import *

class GraphIt(Graph):
    '''Реалізує граф з ітератором по вершинах.

    '''
    def __iter__(self):
        '''Повернути елемент.
        '''
        for k in self.nodes():
            yield k

    def hdegin(self, key):
        '''Напівстепінь входу вершини.
        '''
        return len(self.getpredecessors(key))

    def hdegout(self, key):
        '''Напівстепінь виходу вершини.
        '''
        return len(self.getsucceders(key))

