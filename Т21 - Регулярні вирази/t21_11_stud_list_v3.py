#T21_11_v3
#Список з даними про студентів
#Завдання одного шаблону для рядка файлу.
#Пошук входження та підгрупи
#Різні формати дати
#Різні формати телефонів та приведення телфону до канонічного вигляду
#Збереження результатів та помилкових записів у файли

import re
import datetime
import pickle

P_NAME = r'(\b[А-ЯҐЄІЇ][А-ЯҐЄІЇа-яґєії]*)'
P_STUD_PASS = r'([А-ЯҐЄІЇ|A-Z]{2}\d{8})'
P_PHONE = r'''(\+380\s\(\d{2}\)\s\d{3}\s\d{4}   # номер у 'канонічному вигляді'
            |\D?380\D{0,2}\d{2}\D{0,2}\d{3}\D?\d{2}\D?\d{2} # номер з кодом країни 
            |\b0\d{2}\D?\d{3}\D?\d{2}\D?\d{2})  # номер без коду країни
            '''
P_DATE = r'''(\d{1,2}\.\d{1,2}\.\d{4}   # дата розділена крапками dd.mm.yyyy
             |\d{4}-\d{1,2}-\d{1,2}     # дата розділена мінусами yyyy-mm-dd
             |\d{1,2}/\d{1,2}/\d{4})    # дата розділена косими рисками mm/dd/yyyy
             '''
P_STUD = r'\s'.join([P_NAME,P_NAME,P_NAME,P_STUD_PASS,P_DATE,P_PHONE])

def process_file(fname, errname):
    '''Обробляє файл fname з відомостями про студентів

    Очікуваний формат даних, наприклад:
    Іваненко Іван   Іванович  АБ23445645 14.02.1998 +380 (50) 234 4567
    Неправильні рядки записує у файл errname
    '''
    students = {}                       # словник з даними студентів
    pat_stud = re.compile(P_STUD, re.VERBOSE)
    g = open(errname, "w")
    errcount = 0
    f = open(fname,"r")
    for line in f:
        try:
            process_line(line, students, pat_stud)    # обробити 1 рядок файлу
        except ValueError:
            errcount += 1
            g.write(line)
    if errcount != 0:
        print("Неправильних записів:", errcount)
    f.close()
    g.close()
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

def getphone(phone):
    '''Повертає номер телефону в канонічному вигляді: +380 (XX) XXX XXXX.'''
    phone = re.sub('\D', '', phone) # забрати всі нецифрові символи
    if len(phone) < 12:
        phone = '38' + phone
    phone = '+{} ({}) {} {}'.format(phone[:3], phone[3:5], phone[5:8], phone[8:])
    return phone
    
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
    bdate = getdate(st[4])          # дата народження

    # привести телефон до канонічного вигляду
    phone = getphone(st[5]) 

    # записати дані студента у словник
    students[key] = (st[0], st[1], st[2], bdate, phone)

if __name__ == '__main__':
    filename = input("Ім'я файлу: ")
    errname = 'errdata.txt'
    students = process_file(filename, errname)
    # збереженя оброблених даних у файлі
    archname = filename + '.dat'
    h = open(archname, "wb")
    pickle.dump(students, h)
    h.close
    # читання збережених даних з файлу
    h = open(archname, "rb")
    students = pickle.load(h)
    h.close

    for a in students:
        print(a, students[a])
