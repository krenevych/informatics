#t24_41_grid_canvas.py
# Клас GridCanvas для зображення поля у клітинку заданого розміру rows x cols

from abc import ABC, abstractmethod
import tkinter as tk


ANIMATION_DELAY = 2 # затримка анімації у мілісікундах


class BoundObj(ABC):
    """
    Абстрактний клас об'єкта, який прив'язано до клітинки поля row  col.

    self.master - охоплюючий об'єкт - поле у клітинку
    self.row - номер рядка
    self.col - номер стовпчика
    self.width - ширина клітинки
    self.height - висота клітинки
    self.ratio - доля клітинки, яка має бути заповнена об'єктом (від 0 до 1)
    self.fill - колір заповнення
    self.outline - колір границі
    self.features - додаткові характеристики об'єкту
    """
    def __init__(self, master, row, col, width, height, ratio,
                 fill='black', outline='', **features):
        self.master = master
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.ratio = ratio
        self.fill = fill
        self.outline = outline
        self.features = features
        self.rect = self._get_rect()

    def _get_rect(self):
        # визначаємо охоплюючий прямокутник
        r2 = (1 - self.ratio) / 2
        top = self.row * self.height     # лівий верхній кут зображення (y)
        left = self.col * self.width     # лівий верхній кут зображення (х)
        xmin = left + int(self.width * r2)
        ymin = top + int(self.height * r2)
        xmax = left + int(self.width * (1 - r2))
        ymax = top + int(self.height * (1 - r2))
        return xmin, ymin, xmax, ymax

    @abstractmethod
    def move(self, dx, dy):
        """
        Перемістити об'єкт на dx, dy пікселів.
        """
        pass

    @abstractmethod
    def delete(self):
        """
        Видалити об'єкт.
        """
        pass

    @abstractmethod
    def coords(self):
        """
        повернути координати об'єкту
        """
        pass


class BoundOval(BoundObj):
    """
    Клас овал, який прив'язано до клітинки поля.
    self.master - охоплюючий об'єкт - поле у клітинку
    self.id - ідентифікатор об'єкту на полотні
    """
    def __init__(self, master, row, col, width, height, ratio,
                 fill='black', outline='', **features):
        BoundObj.__init__(
            self, master, row, col, width, height, ratio,
            fill=fill, outline=outline, **features)
        if not self.outline:
            self.outline = self.fill
        xmin, ymin, xmax, ymax = self.rect
        self.id = master.create_oval(
            xmin, ymin, xmax, ymax, fill=self.fill,
            outline=self.outline, **features)

    def move(self, dx, dy):
        """
        Перемістити об'єкт на dx, dy пікселів.
        """
        self.master.move(self.id, dx, dy)

    def delete(self):
        """
        Видалити об'єкт.
        """
        self.master.delete(self.id)

    def coords(self):
        """
        повернути координати об'єкту
        """
        return self.master.coords(self.id)


class GridCanvas(tk.Canvas):
    """
    Клас для зображення поля у клітинку заданого розміру rows x cols.

    Клас є нащадком Canvas.
    self.rows - кількість рядків поля
    self.cols - кількість стовпчиків поля
    self.selection_handler - функція, що буде викликатись при виборі
                            клітинки поля
    self.bordercolor - колір границі між клітинками
    self.evenbg - колір заповнення клітинок з парними номерами
                  (якщо відрізняється для парних та непарних номерів).
                  Перша клітинка має номер 0
    self.highlightbg - колір заповнення вибраної клітинки
    self.ratio - відсоток заповнення площі клітинки зв'язаним об'єктом
    self.cellwidth - ширина клітинки
    self.cellheight - висота клітинки
    self.grid - матриця, що складається зі зв'язаних об'єктів
                для всіх клітинок. Якщо до клітинки не први'язано
                об'єкт, то значення відповідного елемента - None.
    self.moved - змінна tkinter для контролю завершення переміщення
    """

    def __init__(self, master, rows, cols, selection_handler, *args,
                 bordercolor='black', evenbg='', ratio = 0.85,
                 highlightbg='grey', **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.rows = rows
        self.cols = cols
        self.selection_handler = selection_handler
        self.bordercolor = bordercolor
        self.evenbg = evenbg
        self.highlightbg = highlightbg
        self.ratio = ratio

        self.cellwidth = int(self['width']) // self.cols
        self.cellheight = int(self['height']) // self.rows
        # заповнити матрицю зв'язаних об'єктів значенням None
        self.grid = [[None] * cols for row in range(rows)]
        # зобразити поле
        self._drawgrid()
        # прив'язати подію натиснення лівої клавіші миші над клітинкою поля
        self.bind('<Button-1>', self.on_click)
        self.moved = tk.IntVar()
        self.moved.set(1)

    def _tagstr(self, row, col):
        """
        Побудувати рядок з тегом для клітинки (row, col).
        Наприклад: 't001002'
        """
        return f't{row:0>3}{col:0>3}'

    def _drawgrid(self):
        """Зобразити поле з прямокутників.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                # визначити границі прямокутника
                # для клітинки (row, col)
                xstart = col * self.cellwidth
                ystart = row * self.cellheight
                xend = xstart + self.cellwidth + 1
                yend = ystart + self.cellheight + 1
                # визначити колір заповнення
                bg = self.evenbg if self.evenbg and (row + col) % 2 == 0 \
                    else self['bg']
                # зобразити прямокутник та встановити його тег
                self.create_rectangle(
                    xstart, ystart, xend, yend, width=self['bd'], fill=bg,
                    outline=self.bordercolor, tags=self._tagstr(row, col))
        
    def create_bound(self, klass, row, col, fill='black',
                     outline='', **features):
        """
        Створити та зобразити зв'язаний об'єкт для row, col.

        klass - клас об'єкту, що буде зображено
        fill, outline - кольори заповнення та границі
        features - додаткові характеристики об'єкту
        """
        self.grid[row][col] = klass(
            self, row, col, self.cellwidth, self.cellheight, self.ratio,
            fill=fill, outline=outline, **features)

    def delete_bound(self, row, col):
        """Видалити зв'язаний об'єкт для row, col."""
        bo = self.grid[row][col]
        if bo:
            bo.delete()
            self.grid[row][col] = None

    def _movestep(self, bo, ddx, ddy, xfinal, yfinal):
        """
        Зробити 1 крок для "повільного" пересування об'єкту.

        bo - зв'язаний об'єкт,
        ddx, ddy - кроки по x, y,
        xfinal, yfinal - кінцеві координати лівого верхнього кута
        """
        x, y, mx, my = bo.coords() # отримати поточні координати
        # обчислити нові значення ddx, ddy
        if x == xfinal:
            ddx = 0
        if y == yfinal:
            ddy = 0
        if ddx or ddy: # якщо не дійшли до кінця
            bo.move(ddx, ddy) # перемістити об'єкт
            # встановити виклик переміщення на наступний крок
            # через 5 мілісекунд
            self.after(
                ANIMATION_DELAY, self._movestep, bo, ddx, ddy, xfinal, yfinal)
        else:
            # змінити self.moved, щоб зафіксувати завершення переміщення
            self.moved.set(1)

    def move_bound(self, fromrow, fromcol, torow, tocol, slow=False):
        """
        Пересування об'єкту.

        fromrow, fromcol - початкова клітинка,
        torow, tocol - кінцева клітинка,
        slow - пересувати повільно
        """
        # визначити зсув по x, y
        dx = (tocol - fromcol) * self.cellwidth
        dy = (torow - fromrow) * self.cellheight
        bo = self.grid[fromrow][fromcol] # отримати зв'язаний об'єкт
        if not bo or (dx == 0 and dy == 0): # немає що і куди переміщувати
            return

        if slow: # якщо пересувати повільно
            # встановити зсув на 1 крок рівним 1, 0 або -1
            # у залежності від dx, dy
            ddx = _sign(dx)
            ddy = _sign(dy)
            # обчислити фінальні координати
            xfinal = tocol * self.cellwidth + \
                     int(self.cellwidth * (1 - self.ratio) / 2)
            yfinal = torow * self.cellheight + \
                     int(self.cellheight * (1 - self.ratio) / 2)
            # запустити анімацію пересування
            self.moved.set(0)
            self._movestep(bo, ddx, ddy, xfinal, yfinal)
            # очікувати зміни значення self.moved
            self.wait_variable(self.moved)
        else:
            # пересунути одразу на dx, dy
            bo.move(dx, dy)
        # переприв'язати об'єкт
        self.grid[fromrow][fromcol] = None
        self.grid[torow][tocol] = bo

    def select_cell(self, row, col):
        """Вибрати (підсвітити) клітинку row, col."""
        self.itemconfigure(self._tagstr(row, col), fill=self.highlightbg)

    def deselect_cell(self, row, col):
        """Зняти вибір (підсвітчення) клітинки row, col."""
        bg = self.evenbg if self.evenbg and (row + col) % 2 == 0 \
            else self['bg']
        self.itemconfigure(self._tagstr(row, col), fill=bg)

    def on_click(self, ev):
        """Обробка натиснення лівої клавіші миші."""
        # дозволити обробку подій тільки коли об'єкт не переміщується
        if not self.moved.get():
            return

        # визначити клітинку, де знаходиться миша
        # x = self.canvasx(ev.x) # перевести координати вікна
        # y = self.canvasy(ev.y) # у координати canvas
        row = min(int(ev.y) // self.cellheight, self.rows - 1)
        col = min(int(ev.x) // self.cellwidth, self.cols - 1)
        # викликати функцію обробки вибору клітинки
        self.selection_handler(self, row, col)


def _sign(val):
    "signum(val)"
    return 1 if val > 0 else 0 if val == 0 else -1


# тест модуля
lastrow = 2
lastcol = 2


def sel_handler(gc, row, col):
    """Приклад функції обробки вибору клітинки."""
    global lastrow, lastcol
    gc.deselect_cell(lastrow, lastcol)
    gc.move_bound(lastrow, lastcol, row, col, slow=True)
    gc.select_cell(row, col)
    lastrow = row
    lastcol = col

        
def main():
    """
    Функція для тестування.

    Працює, коли модуль є головним
    """
    top = tk.Tk()
    gc = GridCanvas(top, 8, 8, sel_handler, bordercolor = 'grey',
                    evenbg = 'white',
                    width=350, height=350, bg='black', bd=2)
    gc.pack()
    gc.create_bound(BoundOval, 2, 2, fill='red')
    tk.mainloop()


if __name__ == '__main__':
    main()
