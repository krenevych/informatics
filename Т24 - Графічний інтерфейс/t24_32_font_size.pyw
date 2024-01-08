#t24_32
# Клас для зміни розміру та написання шрифта

from tkinter import *

class FontOpts:
    '''Клас для зміни розміру та написання шрифта.

       self.top - вікно верхнього рівня у якому розміщено елементи
       self.cancel - чи було натиснуто кнопку "Відмінити"
       self.sizevar - змінна, пов'язана з радіокнопками
       self.boldvar - змінна, пов'язана з 'Напівгрубий'
       self.italicvar - змінна, пов'язана з 'Нахилений'
    '''

    def __init__(self, master):
        self.top = master
        self.cancel = False
        self._make_widgets()

    def _make_widgets(self):
        '''Створити елементи для зміни розміру та написання шрифта.
        '''
        # рамка та радіокнопки розміру шрифта
        fsizeopts = Frame(self.top)
        fsize = LabelFrame(fsizeopts, text='Розмір шрифта')
        sizes = [10, 12, 14, 16, 20]
        self.sizevar = IntVar() # змінна, пов'язана з радіокнопками
        for sz in sizes:
            s = str(sz)
            Radiobutton(fsize, text=s,
                        variable=self.sizevar,
                        value=sz).pack(anchor=NW)
        self.sizevar.set(sizes[0]) # увімкнути кнопку "10"
        fsize.pack(side=LEFT, fill=BOTH, expand=YES)

        # рамка та кнопки вибору параметрів шрифта
        fopts=LabelFrame(fsizeopts, text='Написання') 
        self.boldvar = IntVar() # змінна, пов'язана з 'Напівгрубий'
        Checkbutton(fopts, text='Напівгрубий',
                    variable=self.boldvar).pack(anchor=NW)
        self.italicvar = IntVar() # змінна, пов'язана з 'Нахилений'
        Checkbutton(fopts, text='Нахилений',
                    variable=self.italicvar).pack(anchor=NW)
        fopts.pack(side=LEFT, fill=BOTH, expand=YES)
        fsizeopts.pack(side=TOP, fill=BOTH, expand=YES)
                        
        # рамка та кнопки 'Ok' та 'Відмінити'
        fbut = Frame(self.top)
        bcancel = Button(fbut,
                        text='Відмінити',
                        command=self.cancel_handler).pack(
                            side=RIGHT, padx=5, pady=5)
        bok = Button(fbut, text='Ok',
                        command=self.ok_handler).pack(
                            side=RIGHT, padx=5, pady=5)
        fbut.pack(side=TOP, fill=X, expand=YES)

    def ok_handler(self, ev=None):
        '''Обробити натиснення кнопки "Ok".'''
        self.top.destroy()   # закрити вікно self.top
        
    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # відмінити
        self.cancel = True
        self.ok_handler(ev)

    def get(self):
        '''Повернути розмір та написання шрифта.

           Якщо натиснуто "відмінити", то повертає (None, None).
        '''
        if not self.cancel:
            # отримати значення змінних, пов'язаних з кнопками
            size = self.sizevar.get()
            bold = self.boldvar.get()
            italic = self.italicvar.get()
            if bold and italic:
                opts = "bold italic"
            elif bold:
                opts = "bold"
            elif italic:
                opts = "italic"
            else:
                opts = "normal"
        else:
            size = opts = None
        return size, opts
        
        
def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    f = FontOpts(top)
    mainloop()
    print(f.get())
    

if __name__ == '__main__':
    main()
