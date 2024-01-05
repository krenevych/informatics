#T14s3_01
#Бінарне дерево


class Btree:
    '''Реалізує бінарне дерево.
    '''
    def __init__(self):
        '''Створити порожнє дерево.
        '''
        self._data = None       #навантаження кореня дерева
        self._ls = None         #лівий син
        self._rs = None         #правий син

    def isempty(self):
        '''Чи порожнє дерево?.
        '''
        return self._data == None and self._ls == None and self._rs == None

    def maketree(self, data, t1, t2):
        '''Створити дерево.

        Дані у корені - data, лівий син - t1, правий син - t2
        '''
        self._data = data
        self._ls = t1
        self._rs = t2

    def root(self):
        '''Корінь дерева.
        '''
        if self.isempty():
            print('root: Дерево порожнє')
            exit(1)
        return self._data

    def leftson(self):
        '''Лівий син.
        '''
        if self.isempty():
            t = self
        else:
            t = self._ls
        return t

    def rightson(self):
        '''Правий син.
        '''
        if self.isempty():
            t = self
        else:
            t = self._rs
        return t

    def updateroot(self, data):
        '''Змінити корінь значенням data.
        '''
        if self.isempty(): #якщо дерево порожнє, додати лівого та правого сина
            self._ls = Btree()
            self._rs = Btree()
        self._data = data

    def updateleft(self, t):
        '''Змінити лівого сина значенням t.
        '''
        self._ls = t

    def updateright(self, t):
        '''Змінити правого сина значенням t.
        '''
        self._rs = t

