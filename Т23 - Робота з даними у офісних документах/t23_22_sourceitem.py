#T23_22
# Злиття даних з файлів MS Word, MS Excel за шаблоном MS Word
# Імена полів, що заповнюються даними, мають бути взяті у фігурні дужки { }
# Файли, з яких треба брати дані, вказують у конфігураційному файлі
# Клас SourceItem

class SourceItem:
    '''Джерело даних для злиття а також елемент даних для злиття для деякого поля.

       Призначено для під'єднання до джерела даних та повернення елементів
       даних по кроках.
       self.type - тип джерела даних ('word' чи 'excel')
       self.rootobj - кореневий об'єкт документ (Document) або робоча книга (Workbook)
       self.islead - чи є поле провідним
       self.obj - об'єкт з даними: клітинка аркуша Excel (Cell)
                  або клітинка таблиці Word (_Cell)
       self.parent - об'єкт, що містить self.obj: аркуш Excel (Worksheet)
                  або таблиця Word (Table)
       self.row - поточний рядок, з якого вибираються дані
       self.col - стовпчик, з якого вибираються дані
    '''

    def __init__(self, field, typ, rootobject, islead = False):
        '''Конструктор.

           Здійснює під'єднання до джерела даних.
           rootobject - об'єкт, де розташовано відповідні дані:
           документ (Document) або робоча книга (Workbook),
           в залежності від типу.
           islead - чи є параметр провідним. 
        '''
        self.type = typ
        self.rootobj = rootobject
        self.islead = islead
        self.obj = None
        if self.type == 'excel':
            self._findexcel(field)
        else:
            self._findword(field)
        
    
    def _findexcel(self, field):
        '''Знайти аркуш Excel, стовпчик з даними та початковий рядок для поля field.
        '''
        found = False
        # перебираємо всі аркуші робочої книги Excel
        for sheet in self.rootobj:
            r = sheet.min_row # номер рядка, з якого починаються дані в аркуші
            # шукаємо заголовок, що дорівнює field
            for c in range(sheet.min_column, sheet.max_column + 1):
                if str(sheet.cell(row = r, column = c).value) == field:
                    found = True
                    break
            if found: break
        if not found:
            raise ValueError #change
        # встановлюємо значення для знайденого джерела даних
        self.parent = sheet
        self.row = r
        self.col = c

    def _findword(self, field):
        '''Знайти таблицю Word, стовпчик з даними та початковий рядок для поля field.
        '''
        found = False
        # перебираємо всі таблиці документа Word
        for table in self.rootobj.tables:
            # шукаємо заголовок, що дорівнює field
            for c, cell in enumerate(table.row_cells(0)):
                if cell.text == field:
                    found = True
                    break
            if found: break
        if not found:
            raise ValueError #change
        # встановлюємо значення для знайденого джерела даних
        self.parent = table
        self.row = 0
        self.col = c
            
    def next(self):
        '''Обчислити наступний елемент даних та присвоїти йогог значення self.obj.

           self.obj - об'єкт з даними: клітинка аркуша Excel (Cell)
                  або клітинка таблиці Word (_Cell)
           Якщо виходимо за межі області даних, то:
               якщо поле islead, ініціюємо виключення StopIteration
               якщо поле не islead, то переходимо знову до початку стовпчика з даними
        '''
        self.row += 1
        if self.type == 'excel':
            if self.row > self.parent.max_row: # якщо виходимо за межі області даних
                if self.islead:
                    raise StopIteration
                else:
                    self.row = self.parent.min_row + 1
            self.obj = self.parent.cell(row = self.row, column = self.col)
        else:
            if self.row >= len(self.parent.rows): # якщо виходимо за межі області даних
                if self.islead:
                    raise StopIteration
                else:
                    self.row = 1
            self.obj = self.parent.cell(self.row, self.col)
                
