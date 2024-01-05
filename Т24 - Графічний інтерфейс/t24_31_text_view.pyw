#t24_31
# Клас для перегляду текстових файлів
# Приклад побудови меню та роботи з текстом
# Використовує стандартні діалоги для відкриття файлу та зміни кольору

from tkinter import *
from tkinter.filedialog import askopenfilename 
from tkinter.colorchooser import askcolor
from t24_32_font_size import *

class TextViewer:
    '''Клас для перегляду текстових файлів.

       self.top - вікно верхнього рівня у якому розміщено елементи
       self.filename - ім'я файлу, що переглядається
       self.content - вміст файлу, що переглядається

       self.text - текстовий елемент 
    '''

    def __init__(self, master, filename=None):
        self.top = master
        self.filename = filename
        self._fileopen()
        self._make_widgets()


    def _fileopen(self):
        '''Відкрити файл та прочитати його вміст у self.content.
        '''
        self.content = ''
        if self.filename:
            try:
                with open(self.filename, encoding='utf-8') as f:
                    self.content = f.read()
                self.top.title(self.filename)
            except:
                pass

    def _make_widgets(self):
        '''Створити елементи для перегляду текстів.
        '''
        # заголовок вікна
        self.top.title('Перегляд текстових файлів')

        # меню
        menubar = Menu(self.top)
        # створити меню, що випадає, та додати до головного меню
        # tearoff=0 означає, що меню не може бути "відірване"
        # та переміщуватись у окремому вікні
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Відкрити", command=self.openfile)
        filemenu.add_separator()
        filemenu.add_command(label="Вихід", command=self.top.quit)
        menubar.add_cascade(label="Файл", menu=filemenu)
        # створити меню опцій
        optionsmenu = Menu(menubar, tearoff=0)
        optionsmenu.add_command(label="Шрифт", command=self.setfont)
        optionsmenu.add_command(label="Колір тексту", command=self.fgcolor)
        optionsmenu.add_command(label="Колір фону", command=self.bgcolor)
        menubar.add_cascade(label="Опції", menu=optionsmenu)
        # показати меню
        self.top.config(menu=menubar)

        # рамка, текстове вікно та лінійки прокрутки
        ftext = Frame(self.top)
        self.text = Text(ftext, wrap='none')  # без перенесення тексту  
        sbvert = Scrollbar(ftext, command=self.text.yview)
        sbhor = Scrollbar(ftext, orient=HORIZONTAL, command=self.text.xview)
        sbvert.pack(side=RIGHT, fill=Y)
        sbhor.pack(side=BOTTOM, fill=X)
        self.text.pack(side=TOP, fill=BOTH, expand=YES)
        self.text.config(xscrollcommand=sbhor.set)
        self.text.config(yscrollcommand=sbvert.set)
        ftext.pack(side=TOP, fill=BOTH, expand=YES)
        self._settext() # заповнити вікно текстом з self.content

        # Унеможливлює зміну тексту.
        # Інший варіант - зробити self.text.config(state=DISABLED)
        self.text.bind('<Key>', lambda e: "break")  
        
        
    def _settext(self):
        '''Оновити текст у вікні тексту значенням self.content.'''
        self.text.delete('1.0', END)
        self.text.insert('1.0', self.content)

    def _setcolor(self, whichcolor):
        '''Встановити колір whichcolor.

           whichcolor може дорівнювати 'fg' або 'bg'
        '''
        triple, hexstr = askcolor()
        if hexstr:
            self.text[whichcolor]=hexstr

    def fgcolor(self):
        '''Встановити колір тексту.'''
        self._setcolor('fg')

    def bgcolor(self):
        '''Встановити колір фону.'''
        self._setcolor('bg')

    def setfont(self):
        '''Встановити розмір та написання шрифту.'''
        dialog = Toplevel()
        fo = FontOpts(dialog)
        # зробити діалог модальним
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()
        size, opts = fo.get()
        if size:
            family = self.text['font'][0]
            self.text['font'] = (family, size, opts)

    def openfile(self):
        '''Встановити ім'я файлу та відкрити файл.'''
        filename = askopenfilename() # стандартний діалог відкриття файлу
        if filename:
            self.filename = filename
            self._fileopen()
            self._settext()

        
def main():
    '''Функція для тестування.

       Працює, коли модуль є головним
    '''
    top = Tk()
    t = TextViewer(top)
    mainloop()

if __name__ == '__main__':
    main()
