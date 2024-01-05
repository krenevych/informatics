#T21_11_v1
#Список з даними про студентів

import re
import datetime

P_NAME = r'\b[A-Z][a-z]*\b'
P_STUD_PASS = r'[А-ЯҐЄІЇ|A-Z]{2}\d{8}'
P_PHONE = r'\+380\s\(\d{2}\)\s\d{3}\s\d{4}'
P_DATE = r'\d{2}\.\d{2}\.\d{4}'

def process_file(fname):
    '''Обробляє файл fname з відомостями про студентів

    Очікуваний формат даних, наприклад:
    Іваненко Іван   Іванович  АБ23445645 14.02.1998 +380 (50) 234 4567
    '''
    students = {}                       # словник з даними студентів
    f = open(fname,"r")
    for line in f:
        process_line(line, students)    # обробити 1 рядок файлу
    f.close()
    return students

def process_line(line, students):
    '''Обробляє рядок line з відомостями про студентів та додає його
    до словника students.

    Очікуваний формат даних, наприклад:
    Іваненко Іван   Іванович  АБ23445645 14.02.1998 +380 (50) 234 4567
    '''
    x = line.split()            
    line = ' '.join(x)                      # залишити по 1 пропуску між словами
    names123 = re.findall(P_NAME, line)     # знайти прізвище, ім'я, по батькові
#    print(names123)
    found = len(names123) == 3
    stud_pass = re.findall(P_STUD_PASS, line) # знайти номер студентського квитка
#    print(stud_pass)
    found = found and len(stud_pass) == 1
    bdates = re.findall(P_DATE, line)       # знайти дату народження
#    print(bdates)
    found = found and len(bdates) == 1
    phone = re.findall(P_PHONE, line)       # знайти телефон
#    print(phone)
    found = found and len(phone) == 1
    if not found:                           # якщо є хоча б одна помилка
        raise ValueError("Неправильний формат даних '{}'".format(line))
    # записати дані студента у словник
    students[stud_pass[0]] = (names123, bdates, phone[0])
    
if __name__ == '__main__':
    filename = input("Ім'я файлу: ")
    students = process_file(filename)
    for a in students:
        print(a, students[a])
