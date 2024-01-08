#T23_11
# Клас редактор словника

from tkinter import *

class DictEditor:
    '''Клас призначено для редагування словника.

       Визначає кількість ключів та створює елементи для редагування.
       self.master - вікно, у якому розміщується вікно редагування.
       self.dct - словник, що редагується
       self.has_buttons - чи є власні кнопки у вікна редагування
       self.vars - словник з текстовими змінними для зв'язування
                   з полями введення
       self.labels - словник з надписами
       self.entries - словник з полями введення
       Ключі у всіх словниках такі ж, як і у словнику, що редагується  
    '''
    def __init__(self, master, dct, has_buttons=True):
        self.master = master
        self.dct = dct
        self.has_buttons = has_buttons
        self._make_widgets()

    def _make_widgets(self):
        '''Створити елементи інтерфейсу для редагування словника.'''
        # рамка для полів введення
        self.fedit = Frame(self.master, bd=1, relief=SUNKEN) 
        self._make_entries()
        self._layout_entries()
        if self.has_buttons:
            fbut = Frame(self.master)   # рамка з кнопками
            fbut.grid(row=1, column=0, sticky=(E, W))
            # кнопка 'Відмінити'
            bcancel = Button(fbut, text = 'Відмінити',
                   command = self.cancel_handler)
            bcancel.grid(row=0,column=1, sticky=(E), padx=5, pady=5)
            # кнопка 'Ok'
            bok = Button(fbut, text = 'Ok',
                   command = self.ok_handler)
            bok.grid(row=0,column=0, sticky=(E), padx=5, pady=5)
            # забезпечити зміну розмірів області кнопок
            fbut.columnconfigure(0, weight=1)

    def _make_entries(self):
        '''Створити надписи та поля введення.'''
        self.vars = {}
        self.labels = {}
        self.entries = {}
        for key in self.dct:
            # додати надпис до словника надписів
            self.labels[key] = Label(self.fedit, text = str(key))
            # створити текстову змінну для поля введення
            # та встановити її початкове значення
            self.vars[key] = StringVar()
            self.vars[key].set(self.dct[key])
            # додати поле введення та зв'язати з текстовою змінною
            self.entries[key] = Entry(self.fedit,
                                      textvariable = self.vars[key])

    def _layout_entries(self):
        '''Розмістити надписи та поля введення.'''
        for i, key in enumerate(self.dct):
            # розмістити надписи у першому стовпчику
            self.labels[key].grid(row=i, column=0,
                                  sticky=(W), padx=1, pady=1)
            # розмістити поля введення у другому стовпчику
            self.entries[key].grid(row=i, column=1,
                                   sticky=(W, E), padx=1, pady=1)
        # розташувати рамку у вікні self.master
        self.fedit.grid(row=0, column=0, sticky=(W,E,N,S)) 
        # забезпечити зміну розмірів рамок з елементами та кнопками    
        self.master.columnconfigure(0, weight=1)
        # забезпечити зміну розмірів області елементів    
        self.fedit.columnconfigure(0, weight=1)
        self.fedit.columnconfigure(1, weight=2)

    def ok_handler(self, ev=None):
        '''Обробити натиснення кнопки "Ok".'''
        self.master.destroy()   # закрити вікно self.master
        
    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # встановити початкові значення усіх текстових змінних
        # тобто, відмінити усі зміни
        for key in self.vars:
            self.vars[key].set(self.dct[key])
        self.master.destroy() # закрити вікно self.master

    def get(self):
        '''Повернути у словнику rezult значення усіх полів введення.'''
        result = {}
        for key in self.vars:
            result[key] = self.vars[key].get()
        return result
        

if __name__ == '__main__':    
    d = {'banana':3, 'orange':5, 'watermelon':2}
    top = Tk()                          # створення вікна
    de = DictEditor(top, d)             # створити об'єкт DictEditor
    top.mainloop()
    d = de.get()                        # отримати значення словника
    print(d)
    
