#t24_21
# Клас для перегляду вмісту каталогів та вибору каталогу
# Перероблено на основі Wesley J. Chun - Core Python Programming

import os
import sys
from tkinter import *
from tkinter.messagebox import *

class DirSelector:
    '''Клас для вибору каталогу зі списку каталогів.

       self.top - вікно верхнього рівня у якому розміщено елементи
                  з вибору каталогу
       self.cwd - поточний каталог. Змінюється під час вибору
       self.oldcwd - попередній поточний каталог для відновлення
                  значення поточного каталогу після вибору
       self.result - каталог, що вибрано. Якщо не вибрано жодного, то ''

       self.dirfl     - рамка для імені поточного каталогу
       self.dirl      - надпис - ім'я поточного каталогу
       self.dirfm     - рамка для списку та лінійки прокрутки
       self.dirsb     - лінійка прокрутки
       self.dirs      - список каталогів
       self.bfm       - рамка для кнопок
       self.bok       - кнопка 'Ok',
       self.bcancel   - кнопка 'Відмінити'
    '''

    def __init__(self, master, initdir=None):
        self.top = master

        self.oldcwd = os.getcwd()
        self.result = ''
        # визначаємо початковий каталог
        if not initdir or not os.path.exists(initdir):
            self.cwd = os.curdir
        else:
            self.cwd = initdir
        # створюємо елементи
        self._make_widgets()

        self.doLS()

    def _make_widgets(self):
        '''Створити елементи для вибору каталогу.
        '''
        # рамка та надпис з ім'ям каталогу
        self.dirfl = Frame(self.top)
        self.dirl = Label(self.dirfl, 
                font=('Helvetica', 12, 'bold'))
        self.dirl.pack(side=LEFT, fill=X)
        self.dirfl.pack(side=TOP, fill=X, expand=YES)

        # рамка, список та лінійка прокрутки
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15,
                    width=50, yscrollcommand=self.dirsb.set)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=RIGHT, fill=BOTH, expand=YES)
        self.dirfm.pack(side=TOP, fill=BOTH, expand=YES)
        # зв'язати подвійне натиснення лівої клавіші миші
        # з функцією обробки self.setDirAndGo
        self.dirs.bind('<Double-1>', self.setDirAndGo)

        # рамка та кнопки
        self.bfm = Frame(self.top)
        self.bok = Button(self.bfm, text='Ok',
                        command=self.ok_handler)
        self.bcancel = Button(self.bfm,
                        text='Відмінити',
                        command=self.cancel_handler)
        self.bcancel.pack(side=RIGHT, padx=5, pady=5)
        self.bok.pack(side=RIGHT, padx=5, pady=5)
        self.bfm.pack(fill=X, expand=YES)
        self.dirs.config(selectbackground='LightSkyBlue')
        

    def setDirAndGo(self, ev=None):
        '''Обробити подвійне натиснення лівої клавіші миші.'''
        temp = self.cwd # запам'ятати поточний каталог
        try:
            # отримати вибраний елемент списку
            check = self.dirs.get(self.dirs.curselection())
            if not check:
                check = os.curdir
            self.cwd = check
            # оновити список каталогів
            self.doLS()
        except TclError:
            # пропустити помилку curselection, якщо під час
            # подвійного натиснення лівої клавіші миші список порожній
            pass
        except Exception as e:
            # якщо інша помилка, то видати повідомлення
            showwarning('Помилка', e)
            self.cwd = temp             # відновити поточний каталог
            
    def _isroot(self, directory):
        '''Перевірити, чи є поточний каталог кореневим на диску.'''
        if sys.platform.startswith('win'):
            # якщо windows
            isroot = directory.endswith(':\\')
        else:
            # якщо unix, linux, mac os
            isroot = directory == '/'
        return isroot

    def _getdriveslist(self):
        '''Повернути список дисків (точок монтування).'''
        if sys.platform.startswith('win'):
            # якщо windows
            driveslist = [chr(i) + ":\\" for i in range(ord('A'),ord('Z') + 1)
                                if os.path.exists(chr(i) + ":\\")]
        elif sys.platform.startswith('darwin'):
            # якщо mac os
            driveslist = os.listdir('/volumes')
        else:
            # якщо unix, linux
            driveslist = os.listdir('/mnt')
        return driveslist
                          
    def doLS(self):
        '''Оновити список каталогів.'''
        
        if self.cwd == os.pardir and self._isroot(self.result):
            # якщо поточний каталог кореневий, сформувати список дисків
            self.dirs.delete(0, END)            # очистити список на екрані
            self.top.update()                   # оновити зображення
            dirlist = self._getdriveslist()
            self.cwd = ''
            # запам'ятати результат вибору
            self.result = ''
        else:
            # інакше сформувати список підкаталогів поточного каталогу 
            dirlist = []
            for d in os.listdir(self.cwd):
                fullitem = os.path.join(self.cwd, d)
                if os.path.isdir(fullitem):
                    dirlist.append(d)
            dirlist.sort()
            os.chdir(self.cwd)  # змінити поточний каталог
            # запам'ятати результат вибору
            self.result = os.getcwd()
            self.dirs.delete(0, END)            # очистити список на екрані

        # відобразити змінений каталог у надписі
        self.dirl.config(text=self.result)
        # змінити вміст списку
        if self.cwd:                 # якщо список - це не список дисків
            self.dirs.insert(END, os.curdir)    # вставити поточний каталог (.)
            self.dirs.insert(END, os.pardir)    # вставити батьківський каталог (..)
            self.cwd = os.curdir
        # вставити підкатлоги поточного або диски
        for eachDir in dirlist:
            self.dirs.insert(END, eachDir)

    def ok_handler(self, ev=None):
        '''Обробити натиснення кнопки "Ok".'''
        os.chdir(self.oldcwd)# повернутися до колишнього поточного каталогу
        self.top.destroy()   # закрити вікно self.top
        
    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # відмінити усі зміни
        self.result = ''
        self.ok_handler(ev)

    def get(self):
        '''Повернути вибраний каталог.

           Якщо каталог не вибрано, то повертається порожній рядок.
        '''
        return self.result


def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    d = DirSelector(top, os.curdir)
    mainloop()
    sel = d.get()
    print(sel)

if __name__ == '__main__':
    main()
