#T15_21
#Черга. Обробка виключень

class QueueEmptyError(Exception):
    '''Клас виключення для черги.

    Реалізує виключення у разі спроби взяття елемента
    з порожньої черги.
    '''
    def __init__(self, pname):
        self.pname = pname          #ім'я функції, що ініціювала виключення

    def __str__(self):
        '''Повернути повідомлення про помилку

        '''
        return repr(self.pname) + ". Черга порожня."

class Queue:
    '''Реалізує чергу на базі списку.
    '''
    def __init__(self):
        '''Створити порожню чергу.
        '''
        self._lst = []              #список елементів черги

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
            raise QueueEmptyError('Take')   #ініціювати виключення для порожньої черги 
        data = self._lst.pop(0)             #перший елемент черги - це нульовий елемент списку
        return data

    def __del__(self):
        '''Закінчити роботу з чергою.
        '''
        del self._lst
