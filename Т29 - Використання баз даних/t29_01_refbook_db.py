#t29_01_refbook_db.py
#Телефонний довідник (db)
import sqlite3

class DBRefBook:
    '''Клас для ведення телефонного довідника з використанням бази даних.

       База даних містить 1 таблицю з полями:
        name - ім'я
        phone телефон

       Поля:
       self.filename - ім'я файлу бази даних
    '''
    def __init__(self, filename):
        self.filename = filename

        
    def createrb(self):
        '''Створює довідник та записує у нього n записів.'''
        conn = sqlite3.connect(self.filename)   # зв'язатись з БД
        curs = conn.cursor()                    # створити курсор
        curs.execute('''CREATE TABLE friends
             (name text, phone text)''')
        n = int(input('Кількість записів: '))
        for i in range(n):
            name = input('Прізвище: ')
            phone = input('Телефон: ')
            # вставити запис у таблицю
            curs.execute("INSERT INTO friends VALUES (?, ?)",
                           (name, phone))
        conn.commit()                           # зберегти зміни
        conn.close()                            # розірвати зв'язок

    def apprb(self):
        '''Доповнює довідник одним записом.'''
        conn = sqlite3.connect(self.filename)   # зв'язатись з БД
        curs = conn.cursor()                    # створити курсор
        name = input('Прізвище: ')
        phone = input('Телефон: ')
        # вставити запис у таблицю
        curs.execute("INSERT INTO friends VALUES (?, ?)",
                        (name, phone))
        conn.commit()                           # зберегти зміни
        conn.close()                            # розірвати зв'язок

    def searchrb(self, name):
        '''Шукає у довіднику телефон за ім'ям name.

        Якщо не знайдено, повертає порожній рядок.
        '''
        conn = sqlite3.connect(self.filename)   # зв'язатись з БД
        curs = conn.cursor()                    # створити курсор
        # знайти та повернути потрібний запис
        curs.execute("SELECT phone FROM friends WHERE name=? ", (name, ))
        result = curs.fetchone()
        if result:
            phone = result[0]
        else:
            phone = ""
        conn.close()
        return phone
        
    def replacerb(self, name, newphone):
        '''Замінює у довіднику телефон за ім'ям name на newphone.

        Якщо не знайдено, нічого не робить.
        '''
        conn = sqlite3.connect(self.filename)   # зв'язатись з БД
        curs = conn.cursor()                    # створити курсор
        # знайти та повернути потрібний запис
        curs.execute("SELECT phone FROM friends WHERE name=? ", (name, ))
        result = curs.fetchone()
        if result:
            # внести зміни до таблиці БД
            curs.execute("UPDATE friends SET phone=? WHERE name=?",
                         (newphone, name))
        conn.commit()                           # зберегти зміни
        conn.close()                            # розірвати зв'язок

        
    
filename = 'refs.db'                #ім'я файлу БД довідника

rb = DBRefBook(filename)

while True:
    k = int(input('Режим роботи [1 - 5]:'))
    if k == 1:                      #створити довідник 
        rb.createrb()
    elif k == 2:                    #додати запис до довідника 
        rb.apprb()
    elif k == 3:                    #знайти телефон у довіднику
        name = input('Прізвище: ')
        phone = rb.searchrb(name)
        if len(phone) > 0:
            print('Телефон:', phone)
        else:
            print('не знайдено')
    elif k == 4:                    #замінити телефон у довіднику 
        name = input('Прізвище: ')
        phone = input('Новий телефон: ')
        rb.replacerb(name, phone)
    elif k == 5:
        break
        





      


