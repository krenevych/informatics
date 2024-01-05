#T14s1_01
#Стек на базі списку

class Stack:
    '''Реалізує стек на базі списку.
    '''
    def __init__(self):
        '''Створити порожній стек.
        '''
        self._lst = []          #список елементів стеку

    def isempty(self):
        '''Чи порожній стек?.
        '''
        return len(self._lst) == 0

    def push(self, data):
        '''Вштовхнути елемент у стек.
        '''
        self._lst.append(data)

    def pop(self):
        '''Взяти елемент зі стеку.
        '''
        if self.isempty():
            print('Pop: Стек порожній')
            exit(1)
        data = self._lst.pop()
        return data


#Завершено опис та реалізацію класів

if __name__ == '__main__':
    #Інвертувати послідовність рядків

    st = Stack()
    print('Введіть послідовність рядків. \n"" - кінець введення')

    while True:
        a = input("?")
        if len(a) == 0: break
        st.push(a)              #додаємо рядки до стеку

    print('Послідовність у оберненому порядку')
    while not st.isempty():     #поки стек не порожній
        a = st.pop()            #забираємо верхівку стеку та показуємо
        print(a)

