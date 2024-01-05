#T14s1_21
#Дек


class _Delem:
    '''Реалізує елемент деку.
    '''
    def __init__(self, data):
        '''Створити елемент.
        '''
        self._data = data       #дані, що зберігаються у елементі деку
        self._next = None       #посилання на наступний елемент
        self._prev = None       #посилання на попередній елемент

class Deque:
    '''Реалізує дек без використання списку.
    '''
    def __init__(self):
        '''Створити порожній дек.
        '''
        self._bg = None
        self._en = None

    def isempty(self):
        '''Чи порожній дек?.
        '''
        return self._bg == None and self._en == None

    def putbg(self, data):
        '''Додати елемент до початку деку.
        '''
        elem = _Delem(data)         #створюємо новий елемент деку
        elem._next = self._bg       #наступний елемент для нового - це елемент, який є першим
        if not self.isempty():      #якщо додаємо до непорожнього деку
            self._bg._prev = elem   #новий елемент стає попереднім для першого
        else:
            self._en = elem         #якщо додаємо до порожнього деку, новий елемент буде й останнім
        self._bg = elem             #новий елемент стає першим у деку

    def getbg(self):
        '''Взяти елемент з початку деку.
        '''
        if self.isempty():
            print('getbg: Дек порожній')
            exit(1)
        elem = self._bg             #elem - посилання на перший елемент деку    
        data = elem._data           #запам'ятовуємо дані для поверненя          
        self._bg = elem._next       #першим стає наступний елемент деку
        if self._bg == None:        #якщо в деку був 1 елемент
            self._en = None         #дек стає порожнім
        else:
            self._bg._prev = None   #інакше у новому першому елементі посилання на попередній - None
        del elem                    
        return data

#дії puten та geten повністю симетричні діям putbg та getbg відповідно
    def puten(self, data):
        '''Додати елемент до кінця деку.
        '''
        elem = _Delem(data)
        elem._prev = self._en
        if not self.isempty():
            self._en._next = elem
        else:
            self._bg = elem
        self._en = elem

    def geten(self):
        '''Взяти елемент з кінця деку.
        '''
        if self.isempty():
            print('geten: Дек порожній')
            exit(1)
        elem = self._en
        data = elem._data
        self._en = elem._prev
        if self._en == None:
            self._bg = None
        else:
            self._en._next = None
        del elem
        return data

    def __del__(self):
        '''Закінчити роботу з деком.
        '''
        while self._bg != None:         #проходимо по всіх елементах деку
            elem = self._bg             #запам'ятовуємо посилання на елемент
            self._bg = self._bg._next   #переходимо до наступного елементу
            del elem                    #видаляємо елемент
        self._en = None

def clone(deque):
    resDeque = Deque()
    tmpDeque = Deque()
    while not deque.isempty():
        bg = deque.getbg()
        tmpDeque.puten(bg)
       
    while not tmpDeque.isempty():
        bg = tmpDeque.getbg()
        resDeque.puten(bg)
        deque.puten(bg)
        
    return resDeque; 
