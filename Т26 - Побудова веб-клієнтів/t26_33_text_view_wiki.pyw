#t26_33
# Клас для перегляду текстових файлів та показу визначення з Вікіпедії

from tkinter import *
from tkinter.messagebox import *
from T24.t24_31_text_view import *
from t26_31_wiki_def import *
from t26_32_lang import *

class TextViewerWiki(TextViewer):
    '''Клас для перегляду текстових файлів.

       Додано можливість завантажити з Вікіпедії означення слова чи фрази.
       self.language - мова Вікіпедії
    '''
    def __init__(self, master, filename=None):
        TextViewer.__init__(self, master, filename)
        self.language = 'uk'


    def _make_widgets(self):
        '''Створити меню Вікі.
        '''
        TextViewer._make_widgets(self)
        # створити меню вікі
        wikimenu = Menu(self.menubar, tearoff=0)
        wikimenu.add_command(label="Вікі", command=self.displaywiki)
        wikimenu.add_command(label="Мова", command=self.setlanguage)
        self.menubar.add_cascade(label="Вікі", menu=wikimenu)
        # показати меню
        self.top.config(menu=self.menubar)
        
    def displaywiki(self):
        '''Показати означення вибраного слова (слів).'''
        if self.text.tag_ranges(SEL): # якщо вибрано текст
            # запам'ятати вибір
            selection = self.text.get(SEL_FIRST, SEL_LAST)
            selection = ' '.join(selection.split()) # видалити зайві пропуски
#            print(selection)
            if selection:
                # запитати означення вікі
                wd = WikiDef(selection, self.language) 
                definition = wd.definition # отримати результат запиту
                if definition:
                    showinfo(selection, definition)
                else:
                    showwarning(selection, 'Не знайдено')

            
    def setlanguage(self):
        '''Встановити мову Вікіпедії.'''
        dialog = Toplevel()
        lo = LangOpts(dialog, self.language)
        # зробити діалог модальним
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()
        lang = lo.get()
        if lang:
            self.language = lang

        
       
def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    t = TextViewerWiki(top)
    mainloop()

if __name__ == '__main__':
    main()
