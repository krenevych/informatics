#T21_11_v2
#Список з даними про студентів
#Завдання одного шаблону для рядка файлу.
#Пошук входження та підгрупи
#Різні формати дати

import re
import datetime

P_NAME = r'(\b[А-ЯҐЄІЇ][А-ЯҐЄІЇа-яґєії]*)'
P_STUD_PASS = r'([А-ЯҐЄІЇ|A-Z]{2}\d{8})'
P_PHONE = r'(\+380\s\(\d{2}\)\s\d{3}\s\d{4})'
P_DATE = r'''(\d{1,2}\.\d{1,2}\.\d{4}   # дата розділена крапками dd.mm.yyyy
             |\d{4}-\d{1,2}-\d{1,2}     # дата розділена мінусами yyyy-mm-dd
             |\d{1,2}/\d{1,2}/\d{4})    # дата розділена косими рисками mm/dd/yyyy
             '''
P_STUD = r'\s'.join([P_NAME,P_NAME,P_NAME,P_STUD_PASS,P_DATE,P_PHONE])

def process_file(fname):
    '''Обробляє файл fname з відомостями про студентів

    Очікуваний формат даних, наприклад:
    Іваненко Іван   Іванович  АБ23445645 14.02.1998 +380 (50) 234 4567
    '''
    students = {}                       # словник з даними студентів
    pat_stud = re.compile(P_STUD, re.VERBOSE)
    f = open(fname,"r")
    for line in f:
        process_line(line, students, pat_stud)    # обробити 1 рядок файлу
    f.close()
    return students

def getdate(datestr):
    '''Повертає дату як об'єкт за рядком дати datestr у різних форматах.

    Можливі формати дати:
    dd.mm.yyyy
    yyyy-mm-dd
    mm/dd/yyyy
    '''
    if '.' in datestr:
        dateformat = "%d.%m.%Y"
    elif '-' in datestr:
        dateformat = "%Y-%m-%d"
    else:                                   # if '/' in datestr:
        dateformat = "%m/%d/%Y"
    return datetime.datetime.strptime(datestr,dateformat)

def process_line(line, students, pat_stud):
    '''Обробляє рядок line з відомостями про студентів та додає його
    до словника students.

    Очікуваний формат даних, наприклад:
    Іваненко Іван   Іванович  АБ23445645 14.02.1998 +380 (50) 234 4567
    '''
    x = line.split()            
    line = ' '.join(x)  # залишити по 1 пропуску між словами
    rez = pat_stud.search(line)     # шукаємо у рядку відповідність шаблону
#    print(rez)
    if rez == None:
        raise ValueError("Неправильний формат даних '{}'".format(line))

    st = rez.groups()               # знайдені підгрупи за шаблоном
#    print(st)
    key = st[3]                     # номер студентського квитка

    # перетворити дату з рядка у формат дати
    bdate = getdate(st[4])                   # дата народження

    # записати дані студента у словник
    students[key] = (st[0], st[1], st[2], bdate, st[5])

if __name__ == '__main__':
    filename = input("Ім'я файлу: ")
    students = process_file(filename)
    for a in students:
        print(a, students[a])
