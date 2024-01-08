#t24_43_lines_gui.pyw
# Клас для зображення інтерфейсу а також для гри у Lines


import tkinter as tk
from tkinter.messagebox import *
from t20_94_grid_canvas import GridCanvas, BoundOval
from t20_95_lines import Lines


# стани
COMPUTER_MOVE = 0   # хід комп'ютера
USER_MOVE = 1       # хід гравця (до вибору кулі)
SELECTED = 2        # хід гравця (після вибору кулі)

class LinesGUI:
    '''
    Клас для реалізації гри у Lines.

    self.top - вікно верхнього рівня у якому розміщено елементи
    self.rows - кількість рядків
    self.cols - кількість стовпчиків
    self.empty - кількість порожніх клітинок на полі
    self.lines - об'єкт класу Lines - містить методи, що підтримують гру
    self.state - стан: хід комп'ютера, хід користувача або вибрано
                клітинку для переміщення
    self.selrow - рядок вибраної клітинки
    self.selcol - стовпчик вибраної клітинки

    self.gc - об'єкт класу GridCanvas - поле з клітинками
    self.little_gc - поле з 3 клітинок для показу наступних кольорів
    self.score - ціла змінна для збереження та відображення рахунку
    '''

    def __init__(self):
        self.top = tk.Tk()
        self.rows = 9
        self.cols = 9
        self.state = COMPUTER_MOVE
        
        # створюємо елементи
        self._make_widgets()
        # розмістити перші три кулі
        self._start_game()

        tk.mainloop()

    def _make_widgets(self):
        '''Створити елементи інтерфейсу Lines.'''
        # заголовок вікна
        self.top.title('Lines')
        # поле у клітинку
        self.gc = GridCanvas(
            self.top, self.rows, self.cols, self.sel_handler,
            width=450, height=450, bordercolor = 'grey', evenbg = '',
            highlightbg = 'light grey', bg='dark slate grey', bd=2)
        self.gc.pack(side=tk.LEFT)
        # рамка для елементів управління: рахунок, кнопка нової гри
        fcntrls = tk.Frame(self.top)
        # маленьке поле у клітинку
        self.little_gc = GridCanvas(
            fcntrls, 1, 3, lambda g, r, c: None, width=120, height=40,
            ratio = 0.5, bordercolor = 'grey', evenbg = '',
            highlightbg = 'light grey', bg='dark slate grey', bd=2)
        self.little_gc.pack(side=tk.TOP, padx=5, pady=5)

        tk.Label(fcntrls, text='Рахунок').pack(side=tk.TOP, fill=tk.X,
                                               padx=5, pady=5)
        self.score = tk.IntVar()
        escore = tk.Entry(
            fcntrls, textvariable=self.score, width = 5, state = 'readonly',
            fg = 'navy', font = ("arial", 16, 'bold'))
        escore.pack(side=tk.TOP, padx=5, pady=5)
        tk.Button(
            fcntrls, text='Нова гра', command=self.newgame_handler)\
            .pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        fcntrls.pack(side=tk.LEFT, fill=tk.BOTH)

    def _start_game(self):
        '''Почати нову гру.'''
        self.empty = self.rows*self.cols
        self.selrow = self.selcol = None
        self.lines = Lines()
        self.score.set(0)
        self.computer_move()

    def move_path(self, path):
        '''
        Перемістити кулю вздовж шляху path.

        path - список клітинок (row, col)
        '''
        fromrow, fromcol = path[0]
        for i in range(1, len(path)):
            torow, tocol = path[i]
            self.gc.move_bound(fromrow, fromcol, torow, tocol, slow=True)
            fromrow, fromcol = torow, tocol

    def clear(self):
        '''Очистити кульки з 5 або більше підряд.'''
        # отримати список клітинок для очищення та додавання до рахунку
        to_clear, addscore = self.lines.clear(self.gc.grid)
        # змінити рахунок
        self.score.set(self.score.get() + addscore)
        cleared = len(to_clear) # кількість клітинок для очищення
        self.empty += cleared
        # очистити клітинки
        for row, col in to_clear:
            self.gc.delete_bound(row, col)
        return cleared
        
    def show_next_colors(self):
        '''Показати кольори кульок для наступного кроку.'''
        grid = self.little_gc.grid
        num = min(3, self.empty)
        for col in range(3):
            self.little_gc.delete_bound(0, col)
        for col in range(num):
            color = self.lines.cl[col]
            self.little_gc.create_bound(
                BoundOval, 0, col, fill=color)

    def computer_move(self):
        '''Розмістити нові кульки та перевірити, чи закінчилась гра.'''
        # отримати нові кулі разом з кольорами
        new_spheres = self.lines.get_spheres(self.gc.grid)
        # розмістити кулі на полі
        for row, col in new_spheres.keys():
            color = new_spheres[(row, col)]
            self.gc.create_bound(
                BoundOval, row, col, fill=color)
        self.empty -= len(new_spheres)  # оновити кількість порожніх клітинок
        # спробувати очистити після ходу комп'ютера
        self.clear()
        if self.empty == 0:
            showinfo(
                f'Кінець гри',
                f'Гру закінчено! рахунок: {self.score.get()}')
        else:
            # показати наступні кольори
            self.show_next_colors()
            # очікувати хід користувача
            self.state = USER_MOVE

    def sel_handler(self, gc, row, col):
        '''Обробити вибір клітинки.'''
        if self.state == COMPUTER_MOVE:
            return

        if self.state == SELECTED: # якщо вибрано клітинку
            # отримати зв'язаний об'єкт
            bo = self.gc.grid[row][col]
            if not bo: # якщо клітинка порожня
                # отримати шлях від раніше вибраної клітинки до даної
                path = self.lines.get_path(
                    self.gc.grid, self.selrow, self.selcol, row, col)
                if path: # якщо є шлях
                    self.state = COMPUTER_MOVE
                    self.gc.deselect_cell(self.selrow, self.selcol)
                    self.move_path(path) # перемістити кулю вздовж шляху
                    cleared = self.clear() # очистити, якщо можливо
                    if not cleared:
                        self.computer_move() # хід комп'ютера
                    else:
                        self.state = USER_MOVE # очікувати хід користувача
                else: # немає шляху - дзвінок
                    self.top.bell()
            else: # якщо клітинка не порожня
                # зробити цю клітинку вибраною
                self.gc.deselect_cell(self.selrow, self.selcol)
                self.selrow = row
                self.selcol = col
                self.gc.select_cell(row, col)
        else: # якщо хід користувача та не вибрано клітинку
            bo = self.gc.grid[row][col]
            if bo: # якщо клітинка не порожня
                # вибрати її
                self.selrow = row
                self.selcol = col
                self.gc.select_cell(row, col)
                self.state = SELECTED

    def newgame_handler(self, ev=None):
        '''Обробити натиснення кнопки "Нова гра".'''
        # очистити поле
        for row in range(self.rows):
            for col in range(self.cols):
                self.gc.delete_bound(row, col)
        if self.selrow is not None:
            self.gc.deselect_cell(self.selrow, self.selcol)
        self.state = COMPUTER_MOVE
        # почати нову гру
        self._start_game()


if __name__ == '__main__':
    lg = LinesGUI()
