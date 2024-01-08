#t24_01_fibgui_v4.pyw
# Обчислення значення числа Фібоначчі. Графічний інтерфейс
# Введення номера числа у графічному режимі
# Встановлення розташування елементів.
# Відступи кнопок. Прив'язка клавіатури. Встановлення "фокусу"

from tkinter import *

def fib(n):
    """Обчислює n-те число Фібоначчі."""
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

def calc(ev = None):
    n = int(ein.get())                      # отримання значення поля введення
    f = fib(n)
    rezult = 'Результат: {}'.format(f)      # побудова рядка для відображення
    lrez.configure(text = rezult)           # зміна надпису значенням результату

def onEscapeKey(event):
    top.quit()

    
top = Tk()                                  # створення вікна

finput = Frame(top)                         # контейнер для надпису та поля введення
finput.pack(fill=X, expand=YES)
Label(finput, text = 'Введіть n: ',
    font=('arial', 16)).pack(side=LEFT)     # створення надпису
                                            # та додавання надпису до вікна
ein = Entry(finput, font=('arial', 16))     # створення поля введення
ein.pack(side=LEFT, fill=X, expand=1)       # додавання поля введення до вікна
ein.focus()                                 # встановлення "фокусу"
                                            # у поле введення

frez = Frame(top)                           # контейнер для надпису результату
frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Результат: ___',
             font=('arial', 16))            # створення надпису
lrez.pack(side=LEFT, fill=X)                # додавання надпису до вікна

fbut = Frame(top)                           # контейнер для кнопок
fbut.pack(side=LEFT, fill=X, expand='1')
bcalc = Button(fbut, text = 'Обчислити',
        command = calc,
        font=('arial', 16))
bcalc.pack(side=LEFT, padx=5, pady=5)       # кнопка "Обчислити"
bquit = Button(fbut, text='Закрити',
        command=top.quit,
        font=('arial', 16))
bquit.pack(side=RIGHT, padx=5, pady=5)      # кнопка "Закрити"

top.bind('<Return>', calc)                  # зв'язування з натисненням клавіш 
top.bind('<Escape>', onEscapeKey)


top.mainloop()
