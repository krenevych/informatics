#t24_42
# Клас для для гри у Lines


import random

# рахунки в залежності від кількості кульок у лінії
scores = {5: 10,
          6: 16,
          7: 22,
          8: 30,
          9: 40}
# кольори кульок
colors = ["yellow", "red", "cyan", "blue", "magenta", "lawn green"]

class Lines:
    '''Клас для підтримки гри у LInes.
        
       self.cl - кольори нових кульок
       self.tries - список можливих переходів у сусідні клітинки
       self.empty_list - список координат порожніх клітинок поля
    '''

    def __init__(self):
        # кольори нових кульок
        self.cl = [random.choice(colors) for i in range(3)]
        self.tries = [(-1,0), (0, -1), (1, 0), (0, 1)]
        self.empty_list = None

    def clear(self, grid):
        '''Очистити кульки з 5 або більше підряд.'''
#        print(grid)
        rows = len(grid)
        cols = len(grid[0])
        addscore = 0  # додавання до рахунку
        to_clear = [] # список координат клітинок, які треба очистити
        # список списків горизонталей
        hors = [[(row, col) for col in range (cols)] for row in range(rows)]
        # список списків вертикалей
        verts = [[(row, col) for row in range (rows)] for col in range(cols)]
        # список списків діагоналей зі спаданням номера рядка
        diags_plusminus = []
        for k in range(rows  + cols - 1):
            row = min(k, rows - 1)
            col = k - row
            lst = []
            for i in range(row + 1):
                if col + i >= cols: break
                lst.append((row - i, col + i))
            diags_plusminus.append(lst)
        # список списків діагоналей зі зростанням номера рядка
        diags_minusplus = [[(rows - row - 1, col) for row, col in lst]
                           for lst in diags_plusminus]
        # список усіх списків
        all_lists = hors + verts + diags_plusminus + diags_minusplus
        for lst in all_lists:
            k = 0
            # знайти 5 або більше однакових клітинок з координатами у списку
            while k <= len(lst) - 5:
                row, col = lst[k]
                bo = grid[row][col]
                if bo:
                    candidate = [(row,col)] # кандидат на видалення
                    color = bo.fill
                    i = 1
                    while k + i < len(lst):
                        row, col = lst[k + i]
                        bo = grid[row][col]
                        if not bo or bo.fill != color: break
                        candidate.append((row,col))
                        i += 1
                    if len(candidate) >= 5:
                        to_clear += candidate # додати до списку на видалення
                        addscore += scores[len(candidate)] # додати рахунок
                    k += i
                else:
                    k += 1
        return to_clear, addscore

    def _set_empty(self, grid):
        '''Отримати список порожніх клітинок.'''
        rows = len(grid)
        cols = len(grid[0])
        self.empty_list = [(row,col) for row in range(rows)
                 for col in range(cols) if not grid[row][col]]


    def get_spheres(self, grid):
        '''Повернути словник з 3 або менше нових кульок.'''
        self._set_empty(grid)
        num = min(3, len(self.empty_list))           # кількість нових кульок
        idx = random.sample(self.empty_list, num)    # координати нових кульок
        # словник з новими кульками
        spheres = {idx[i]:self.cl[i] for i in range(num)}
        # кольори нових кульок для наступного кроку
        self.cl = [random.choice(colors) for i in range(num)]
        return spheres



    def _path_recursive (self, s1, endrow, endcol, path):
        '''Шукає шлях до кінцевої клітинки endrow, endcol.

        path - шлях, список клітинок
        s1 - множина граничних позицій
        s11 - нова множина граничних позицій
        '''
        ok = False
        if (endrow, endcol) in s1:
            ok = True
            path.append((endrow, endcol)) #початок побудови шляху
        elif s1: # якщо гранична множина не порожня
            s11= set()
            #для всіх позицій з множини s1 з усіх можливих кроків
            for (r, c) in s1:    
                for (i,j) in self.tries: #будуємо нову граничну множину s11 
                    row, col = r + i, c + j # робимо крок
                    if (row, col) in self.empty_list:
                        s11.add((row, col))
                        #видаляємо (row, col) з подальшого розгляду
                        self.empty_list.remove((row,col))  
            ok = self._path_recursive(s11, endrow, endcol, path)
            if ok:
                for (i,j) in self.tries:
                    r, c = path[0]
                    row, col = r + i, c + j # робимо крок
                    if (row, col) in s1:
                        path.insert(0,(row, col)) #шлях будується від кінцевої позиції
                        break
                else: # цикл не закінчився break
                    raise ValueError(
                            'Помилка: попередню позицію для {} не знайдено у множині {}'.
                            format(path[0],s1))
        return ok




    def get_path(self, grid, fromrow, fromcol, torow, tocol):
        '''Повернути шлях від (fromrow, fromcol) до (torow, tocol).

           Результат - список кортежів координат клітинок шляху.
           Якщо шляху немає, то повертає порожній список.
        '''
        # отримати список порожніх клітинок
        self._set_empty(grid)
        path = []
        s1 = {(fromrow, fromcol)}
        ok = self._path_recursive (s1, torow, tocol, path)
        return path


if __name__ == '__main__':
    pass
