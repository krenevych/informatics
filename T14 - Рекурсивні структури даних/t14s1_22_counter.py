#T14s1_22
#Лічилка з використанням деку

from t14s1_21_deque import *

class Player:
    '''Реалізує клас Гравець

    n - номер гравця
    '''
    def __init__(self, n):
        self.n = n

    def show(self):
        print(self.n)

def count_counter():
    '''Функція розв'язує задачу "лічилка"
    '''
    d = Deque()                             #створити дек d
    n = int(input('Кількість гравців: '))
    m = int(input('Кількість слів: '))

    for i in range(n):
        pl = Player(i+1)                    #створити гравця з номером на 1 більше i
        d.puten(pl)

    print('\nПослідовність номерів, що вибувають')
    while not d.isempty():
        for i in range(m-1):
            d.puten(d.getbg())              #m-1 раз перекласти гравця з початку до кінця деку
        pl = d.getbg()                      #узяти m-го гравця з початку деку
        pl.show()                           #та показати його номер

count_counter()
