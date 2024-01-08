#t26_32
# Клас для зміни мови Вікіпедії

from tkinter import *

class LangOpts:
    '''Клас для зміни мови.

       self.top - вікно верхнього рівня у якому розміщено елементи
       self.cancel - чи було натиснуто кнопку "Відмінити"
       self.langvar - змінна, пов'язана з радіокнопками
       self.language - мова Вікіпедії (спочатку - початкова мова init_lang)
    '''

    def __init__(self, master, init_lang='uk'):
        self.top = master
        self.cancel = False
        self.language = init_lang
        self._make_widgets()

    def _make_widgets(self):
        '''Створити елементи для зміни мови.
        '''
        # заголовок вікна
        self.top.title('Мова Вікіпедії')
        # радіокнопки мови
        languages = {'uk': 'Українська',
                     'en': 'Англійська',
                     'ru': 'Російська'}
        l_codes = ['uk', 'en', 'ru']  # коди мов для впорядкування кнопок
        self.langvar = StringVar() # змінна, пов'язана з радіокнопками
        for lang in l_codes:
            Radiobutton(self.top, text=languages[lang],
                        variable=self.langvar,
                        value=lang).pack(anchor=NW)
        self.langvar.set(self.language) # увімкнути кнопку, що відповідає
                                        # початковій мові
                       
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
        '''Повернути мову.

           Якщо натиснуто "відмінити", то повертає None.
        '''
        if not self.cancel:
            # отримати значення змінної, пов'язаної з кнопками
            lang = self.langvar.get()
        else:
            lang = None
        return lang
        
        
def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    f = LangOpts(top)
    mainloop()
    print(f.get())
    

if __name__ == '__main__':
    main()
