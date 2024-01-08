#t20_89_double_list.pyw
# Клас для вибору елементів списку та збереження у іншому списку

from tkinter import *
from tkinter.messagebox import *


class DoubleList:
    '''Клас для вибору елементів списку .

       self.top - вікно верхнього рівня у якому розміщено елементи
       self._list_sel - список вибраних елементів
       self._list_all - список усіх елементів
       self._cancel - чи було натиснуто "Відмінити"

       self._l_all - віджет список для всіх елементів
       self._l_sel - віджет список для вибраних елементів
    '''

    def __init__(self, master, list_all, list_sel=None):
        self.top = master
        self._list_sel = list(list_sel) if list_sel else []
        self._list_all = list(set(list_all) - set(list_sel))
        self._list_sel.sort()
        self._list_all.sort()
        self._cancel = False

        self._make_widgets()

    def _make_widgets(self):
        '''Створити елементи для вибору зі списку.
        '''
        # Рамка та список усіх значень
        self._flist_all = Frame(self.top)
        self._sb_all = Scrollbar(self._flist_all)
        self._sb_all.pack(side=RIGHT, fill=Y)
        self._l_all = Listbox(self._flist_all, height=15,
                              width=50, yscrollcommand=self._sb_all.set)
        self._sb_all.config(command=self._l_all.yview)
        self._l_all.pack(side=RIGHT, fill=BOTH, expand=YES)
        self._flist_all.pack(side=LEFT, fill=Y, expand=YES)

        # зв'язати подвійне натиснення лівої клавіші миші
        # з функцією обробки self._right_handler
        self._l_all.bind('<Double-1>', self._right_handler)

        self._fill_list(self._list_all, self._l_all)

        # Рамка та кнопки обміну значень
        self._fbut = Frame(self.top)
        self._b_right = Button(self._fbut, text='   >>   ',
                               command=self._right_handler)
        self._b_left = Button(self._fbut, text='   <<   ',
                              command=self._left_handler)
        self._b_right.pack(side=TOP, padx=5, pady=5)
        self._b_left.pack(side=TOP, padx=5, pady=5)
        self._fbut.pack(side=LEFT, fill=Y, expand=YES)

        # Рамка та список вибраних значень
        self._flist_sel = Frame(self.top)
        self._sb_sel = Scrollbar(self._flist_sel)
        self._sb_sel.pack(side=RIGHT, fill=Y)
        self._l_sel = Listbox(self._flist_sel, height=15,
                              width=50, yscrollcommand=self._sb_sel.set)
        self._sb_sel.config(command=self._l_sel.yview)
        self._l_sel.pack(side=RIGHT, fill=BOTH, expand=YES)
        self._flist_sel.pack(side=LEFT, fill=Y, expand=YES)

        # зв'язати подвійне натиснення лівої клавіші миші
        # з функцією обробки self._right_handler
        self._l_sel.bind('<Double-1>', self._left_handler)

        self._fill_list(self._list_sel, self._l_sel)

        # рамка та кнопки
        self.bfm = Frame(self.top)
        self.bok = Button(self.bfm, text='      Ok      ',
                        command=self.ok_handler)
        self.bcancel = Button(self.bfm,
                        text='Відмінити',
                        command=self.cancel_handler)
        self.bok.pack(side=TOP, padx=5, pady=5)
        self.bcancel.pack(side=TOP, padx=5, pady=5)
        self.bfm.pack(side=LEFT, fill=Y, expand=YES)

    def _fill_list(self, items, lst):
        lst.delete(0, END)  # очистити список на екрані
        for item in items:
            lst.insert(END, item)

    def _right_handler(self, ev=None):
        '''Обробити натиснення кнопки ">>".'''
        try:
            # отримати вибраний елемент списку
            cur_sel = self._l_all.curselection()
            elem = self._l_all.get(cur_sel)
            if not elem:
                return
            index = cur_sel[0]
            # оновити список
            self._l_all.delete(index)
            self._l_sel.insert(END, self._list_all[index])
            self._list_sel.append(self._list_all[index])
            del self._list_all[index]
        except TclError:
            # пропустити помилку curselection, якщо під час
            # подвійного натиснення лівої клавіші миші список порожній
            pass
        except Exception as e:
            # якщо інша помилка, то видати повідомлення
            showwarning('Помилка', e)

    def _left_handler(self, ev=None):
        '''Обробити натиснення кнопки "<<".'''
        try:
            # отримати вибраний елемент списку
            cur_sel = self._l_sel.curselection()
            elem = self._l_sel.get(cur_sel)
            if not elem:
                return
            index = cur_sel[0]
            # оновити список
            self._l_sel.delete(index)
            self._l_all.insert(END, self._list_sel[index])
            self._list_all.append(self._list_sel[index])
            del self._list_sel[index]
        except TclError:
            # пропустити помилку curselection, якщо під час
            # подвійного натиснення лівої клавіші миші список порожній
            pass
        except Exception as e:
            # якщо інша помилка, то видати повідомлення
            showwarning('Помилка', e)

    def ok_handler(self, ev=None):
        '''Обробити натиснення кнопки "Ok".'''
        self.top.destroy()   # закрити вікно self.top
        
    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # відмінити усі зміни
        self._cancel = True
        self.ok_handler(ev)

    def get(self):
        '''Повернути cписок вибраних елементів.

           Якщо каталог не вибрано, то повертається порожній рядок.
        '''
        result = self._list_sel if not self._cancel else None
        return result


def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    d = DoubleList(top, range(10), range(2, 5))
    mainloop()
    sel = d.get()
    print(sel)

if __name__ == '__main__':
    main()
