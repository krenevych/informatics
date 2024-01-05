#T14s1_11
#Черга


class Queue:
    '''Реалізує чергу на базі списку.
    '''
    def __init__(self):
        '''Створити порожню чергу.
        '''
        self._lst = []                   #список елементів черги

    def isempty(self):
        '''Чи порожня черга?.
        '''
        return len(self._lst) == 0

    def add(self, data):
        '''Додати елемент в кінець черги.
        '''
        self._lst.append(data)           

    def take(self):
        '''Взяти елемент з початку черги.
        '''
        if self.isempty():
            print('Take: Черга порожня')
            exit(1)
        data = self._lst.pop(0)         #перший елемент черги - це нульовий елемент списку
        return data

    def __del__(self):
        '''Закінчити роботу з чергою.
        '''
        print('Deleting queue')
        del self._lst
