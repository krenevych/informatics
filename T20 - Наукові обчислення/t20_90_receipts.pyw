#t20_90_receipts.pyw
# Клас для зміни параметрів збереження (backup)

import pickle
from tkinter import *
from t20_86_dicteditor import *
from t20_89_double_list import *
from tkinter.messagebox import *

INGREDIENTS_FILE = "ingredients.txt"

class ReceiptsGUI:
    '''Клас для зміни/створення рецептів.

       self.top - вікно верхнього рівня у якому розміщено елементи
                  інтерфейсу
       self.list_all - список усіх інгредієнтів
       self.ein  - поле введення для назви рецепту
    '''

    def __init__(self, master):
        self.top = master

        with open(INGREDIENTS_FILE, 'r', encoding='utf-8') as f:
            self.list_all = f.readlines()
        self.list_all = list(map(lambda x: x.replace('\n', ''), self.list_all))

        # створюємо елементи
        self._make_widgets()

    def _make_widgets(self):
        '''Створити елементи інтерфейсу backup.
        '''
        # рамка з заголовком для каталогів, що зберігаються
        self.finput = Frame(self.top)  # контейнер для надпису та поля введення
        self.finput.pack(fill=X, expand=YES)
        Label(self.finput, text='Введіть назву рецепту: ',
              font=('arial', 16)).pack(side=LEFT)  # створення надпису
        # та додавання надпису до вікна
        self.ein = Entry(self.finput, font=('arial', 16))  # створення поля введення
        self.ein.pack(side=LEFT, fill=X, expand=1)  # додавання поля введення до вікна
        self.ein.focus()  # встановлення "фокусу"
        # у поле введення

        self.fbut = Frame(self.top)  # контейнер для кнопок
        self.fbut.pack(side=LEFT, fill=X, expand='1')
        self.bcalc = Button(self.fbut, text='Створити/змінити',
                            command=self._create_modify_receipt,
                            font=('arial', 16))
        self.bcalc.pack(side=LEFT, padx=5, pady=5)  # кнопка "Обчислити"
        self.bquit = Button(self.fbut, text='Закрити',
                            command=top.quit,
                            font=('arial', 16))
        self.bquit.pack(side=RIGHT, padx=5, pady=5)  # кнопка "Закрити"

    def _create_modify_receipt(self):
        name = self.ein.get()
        receipt = {}
        try:
            with open(name + '.dat', 'rb') as f:
                receipt = pickle.load(f)
        except (OSError, IOError):
            pass

        dialog = Toplevel()
        dl = DoubleList(dialog, self.list_all, receipt.keys())
        # зробити діалог модальним
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()
        selected = dl.get()
        if not selected:
            return

        sel_dict = {s: "" for s in selected if not s in receipt}
        receipt.update(sel_dict)

        dialog = Toplevel()
        de = DictEditor(dialog, receipt)
        # зробити діалог модальним
        dialog.focus_set()
        dialog.grab_set()
        dialog.wait_window()
        receipt = de.get()
        if receipt:
            showinfo("Рецепт: " + name, receipt)
            with open(name + '.dat', 'wb') as f:
                pickle.dump(receipt, f)

if __name__ == '__main__':
    top = Tk()
    r = ReceiptsGUI(top)
    mainloop()


