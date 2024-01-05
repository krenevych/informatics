#T23_01_v2
# Обчислення значення числа Фібоначчі. Графічний інтерфейс
# Введення номера числа у графічному режимі

from tkinter import *

def fib(n):
    """Обчислює n-те число Фібоначчі."""
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

def calc():
    n = int(ein.get())                      # отримання значення поля введення
    f = fib(n)
    rezult = 'Результат: {}'.format(f)      # побудова рядка для відображення
    lrez.configure(text = rezult)           # зміна надпису значенням результату

def delll():
    top.quit()
    del top
    
top = Tk()                                  # створення вікна

linput = Label(top,
               text = 'Введіть n: ',
               font=('arial', 16))          # створення надпису
linput.pack()                               # додавання надпису до вікна
ein = Entry(top, font=('arial', 16))        # створення поля введення
ein.pack()                                  # додавання поля введення до вікна
lrez = Label(top,
             text='Результат: ___',
             font=('arial', 16),
             fg='cyan', bg = 'navy')        # створення надпису
lrez.pack()                                 # додавання надпису до вікна
bcalc = Button(top, text = 'Обчислити',
              command = calc,
              font=('arial', 16))           # кнопка "Обчислити"
bcalc.pack()
bquit = Button(top, text='Закрити',
              command=delll,
              font=('arial', 16))           # кнопка "Закрити"
bquit.pack(side=LEFT)

top.mainloop()
