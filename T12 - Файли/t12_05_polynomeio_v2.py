#T12_05_v2
#Введення/виведення поліномів з/у текстовий файл
#Використання командного рядка

import sys
import T10.t10_01_polynome as polynome

def fileinputpoly (fname):
    '''Введення поліному з файлу fname.

    '''
    p = {}
    #відкриваємо вхідний файл з ім'ям fname для читання
    f = open(fname,'r')
    for line in f:              #перебираємо всі рядки файлу
        if len(line) > 0:
            x = line.split()    #отримуємо степінь та коефіцієнт
            k = int(x[0])
            c = float(x[1])
            p[k] = c            #записуємо у словник, що зберігає поліном
    if len(p) == 0:
        p[0] = 0
    #закриваємо вхідний файл
    f.close()
    return p

def fileprintpoly (p, fname):
    '''Виведення поліному p у файл fname.

    '''
    #відкриваємо файл з ім'ям fname для запису
    f = open(fname,'w')
    for k in p:         #перебираємо всі одночлени поліному
        #записуємо у файл рядки за допомогою функції format
        print('{0} {1}'.format(k, p[k]), file = f)
    #закриваємо файл
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 4: #якщо вказано неправильну кількість параметрів
        print('usage: t12_05_polynomeio_v2.py filepoly1 filepoly2 filemultpoly')
    else:
        #отримуємо імена 2 вхідних файлів та файлу результату
        name1 = sys.argv[1]
        name2 = sys.argv[2]
        name3 = sys.argv[3]
        #вводимо 2 поліноми з файлів
        p1 = fileinputpoly(name1)
        p2 = fileinputpoly(name2)
        #обчислюємо їх добуток
        p3 = polynome.multpoly(p1,p2)
        #виводимо результат у файл
        fileprintpoly(p3, name3)



      


