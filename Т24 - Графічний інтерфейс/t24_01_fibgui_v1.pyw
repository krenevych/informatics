#T23_01_v1
# Обчислення значення числа Фібоначчі. Графічний інтерфейс

from tkinter import *

def fib(n):
    """Обчислює n-те число Фібоначчі."""
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


n = int(input('Введіть n: '))
f = fib(n)

top = Tk()                              # створення вікна
rezult = 'Fib({}) = {}'.format(n, f)    # побудова рядка для відображення
lrez = Label(top, text = rezult)        # створення надпису
lrez.pack()                             # додавання надпису до вікна



top.mainloop()
