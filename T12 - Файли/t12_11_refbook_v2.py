#T12_11_v2
#Телефонний довідник (shelve)
import shelve

def createrb(filename):
    '''Створює довідник у файлі filename та записує у нього n записів.

    '''
    book = shelve.open(filename)    #відкрити файл зі словником
    n = int(input('Кількість записів: '))

    for i in range(n):
        name = input('Прізвище: ')
        phone = input('Телефон: ')
        book[name] = phone          #додаємо запис      
    book.close()

def apprb(filename):
    '''Доповнює довідник у файлі filename одним записом.

    '''
    book = shelve.open(filename)    #відкрити файл зі словником
    name = input('Прізвище: ')
    phone = input('Телефон: ')
    book[name] = phone              #додаємо запис
    book.close()

def searchrb(filename, name):
    '''Шукає у довіднику у файлі filename телефон за ім'ям name.

    Якщо не знайдено, повертає порожній рядок.
    '''
    book = shelve.open(filename)   #відкрити файл зі словником 
    if name in book:
        phone = book[name]
    else:
        phone = ""
    book.close()
    return phone
    
def replacerb(filename, name, newphone):
    '''Замінює у довіднику у файлі filename телефон за ім'ям name на newphone.

    Якщо не знайдено, нічого не робить.
    '''
    book = shelve.open(filename)    #відкрити файл зі словником
    if name in book:
        book[name] = newphone       #змінюємо запис 
    book.close()
  
    
filename = 'refs.dat'      #ім'я файлу довідника 

while True:
    k = int(input('Режим роботи [1 - 5]:'))
    if k == 1:                      #створити довідник 
        createrb(filename)
    elif k == 2:                    #додати запис до довідника 
        apprb(filename)
    elif k == 3:                    #знайти телефон у довіднику
        name = input('Прізвище: ')
        phone = searchrb(filename, name)
        if len(phone) > 0:
            print('Телефон:', phone)
        else:
            print('не знайдено')
    elif k == 4:                    #замінити телефон у довіднику 
        name = input('Прізвище: ')
        phone = input('Новий телефон: ')
        replacerb(filename, name, phone)
    elif k == 5:
        break
        





      


