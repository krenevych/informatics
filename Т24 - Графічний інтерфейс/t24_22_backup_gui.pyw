#t24_22
# Клас для зміни параметрів збереження (backup)

from tkinter import *
from t24_21_sel_dir import *

class BackupGUI:
    '''Клас для зміни параметрів збереження (backup).

       self.top - вікно верхнього рівня у якому розміщено елементи
                  інтерфейсу
       self.cancel - чи було натиснуто кнопку "Відмінити"
       self.params - словник параметрів, які передаються та повертаються
       self.backupdir - каталог для backup
       self.directories - каталоги, які треба зберігати
       self.interval - інтервал збереження

       self.dirs      - список каталогів
       self.lbdir - надпис за вибраним каталогом, у якому будуть
                    зберігатися файли
       self.eint  - поле введення для інтервалу
    '''

    def __init__(self, master, params):
        self.top = master
        self.cancel = False
        self.params = params
        self._set_params()

        # створюємо елементи
        self._make_widgets()

    def _set_params(self):
        '''Встановити значення окремих параметрів за self.params.
        '''
        self.backupdir = self.params['BackupDirectory']
        self.directories = self.params['Directories'].split()
        self.interval = str(self.params['Interval'])


    def _make_widgets(self):
        '''Створити елементи інтерфейсу backup.
        '''
        # рамка з заголовком для каталогів, що зберігаються
        dirfl = LabelFrame(self.top, text='Каталоги, що зберігаються')
        # рамка, список та лінійка прокрутки
        dirfm = Frame(dirfl)
        dirsb = Scrollbar(dirfm)
        dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(dirfm, height=10,
                    width=50, yscrollcommand=dirsb.set)
        dirsb.config(command=self.dirs.yview)
        for eachDir in self.directories:
            self.dirs.insert(END, eachDir)
        self.dirs.pack(side=RIGHT, fill=BOTH, expand=YES)
        dirfm.pack(side=LEFT, fill=BOTH, expand=YES)
        # рамка та кнопки доавання та видалення
        fbut = Frame(dirfl)
        Button(fbut, text='Додати...',
                    command=self.add_handler).pack(padx=5, pady=5)
        Button(fbut, text='Видалити ',
                    command=self.del_handler).pack(padx=5, pady=5)
        fbut.pack(side=LEFT, fill=Y)
        dirfl.pack(side=TOP, fill=BOTH, expand=YES)

        # рамка та кнопка зміни каталогу для збереження
        fbdir = LabelFrame(self.top, text='Каталог для збереження')
        self.lbdir = Label(fbdir, text=self.backupdir,
                           bd=1, relief=SUNKEN)
        self.lbdir.pack(side=LEFT, fill=X, expand=YES)
        Button(fbdir, text='Змінити...',
                    command=self.change_handler).pack(side=RIGHT,
                                                      padx=5, pady=5)
        fbdir.pack(side=TOP, fill=BOTH, expand=YES)

        # рамка та поле введення інтервалу
        fint = Frame(self.top)
        Label(fint, text='Інтервал (годин)').pack(side=LEFT,
                                                  fill=X)
        self.eint = Entry(fint)
        self.eint.insert(0, self.interval)
        self.eint.pack(side=LEFT, fill=X, expand=YES)
        fint.pack(side=TOP, fill=X, expand=YES)

        # рамка та кнопки 'Старт', 'Відмінити'
        bfm = Frame(self.top)
        Button(bfm, text='Старт',
            command=self.start_handler).pack(side=RIGHT,
                                            padx=5, pady=5)
        Button(bfm, text='Відмінити',
                        command=self.cancel_handler).pack(side=RIGHT,
                                            padx=5, pady=5)
        bfm.pack(fill=X, expand=YES)
        self.dirs.config(selectbackground='LightSkyBlue')
        
    def _select_directory(self):
        '''Створити вікно та запустити вибір каталогів.

           Повернути вибраний каталог
        '''
        dialog = Toplevel()
        ds = DirSelector(dialog)
        # зробити діалог модальним
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()
        return ds.get()


    def add_handler(self, ev=None):
        '''Обробити натиснення кнопки "Додати...".'''
        newdir = self._select_directory()
        if newdir:
            self.dirs.insert(END, newdir)
            self.directories.append(newdir)

    def del_handler(self, ev=None):
        '''Обробити натиснення кнопки "Видалити".'''
        sel = self.dirs.curselection()
        if sel:
            self.dirs.delete(sel[0])
            del self.directories[sel[0]]
        

    def change_handler(self, ev=None):
        '''Обробити натиснення кнопки "Змінити...".'''
        newdir = self._select_directory()
        if newdir:
            self.lbdir['text'] = newdir
            self.backupdir = newdir


    def start_handler(self, ev=None):
        '''Обробити натиснення кнопки "Старт".'''
        self.top.destroy()
        self.top.quit   # закрити вікно self.top
        
    def cancel_handler(self, ev=None):
        '''Обробити натиснення кнопки "Відмінити".'''
        # відмінити
        self.cancel = True
        self.start_handler()

    def get(self):
        '''Повернути параметри.
        '''
        params = {}
        if not self.cancel: # якщо не натиснуто кнопку "Відмінити"
            params['BackupDirectory'] = self.backupdir
            params['Directories'] = ' '.join(self.directories)
            params['Interval'] = self.interval
        return params

