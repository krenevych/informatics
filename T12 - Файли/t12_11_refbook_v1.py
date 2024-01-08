#T12_11_v1
#Телефонний довідник (pickle)
import pickle

def createrb(filename):
    '''Створює довідник у файлі filename та записує у нього n записів.

    '''
    f = open(filename,'wb')
    n = int(input('Кількість записів: '))
    book = {}           #словник, у якому будемо зберігати телефонний довідник

    for i in range(n):
        name = input('Прізвище: ')
        phone = input('Телефон: ')
        book[name] = phone  #додаємо запис
    pickle.dump(book,f)     #записуємо у файл
    f.close()

def apprb(filename):
    '''Доповнює довідник у файлі filename одним записом.

    '''
    f = open(filename,'rb')
    book = pickle.load(f)   #завантажуємо довідник з файлу у словник book
    f.close()
    name = input('Прізвище: ')
    phone = input('Телефон: ')
    book[name] = phone      
    f = open(filename,'wb')
    pickle.dump(book,f)     #записуємо у файл
    f.close()

def searchrb(filename, name):
    '''Шукає у довіднику у файлі filename телефон за ім'ям name.

    Якщо не знайдено, повертає порожній рядок.
    '''
    f = open(filename,'rb')
    book = pickle.load(f)   #завантажуємо довідник з файлу у словник book
    f.close()
    if name in book:
        phone = book[name]
    else:
        phone = ""
    return phone
    
def replacerb(filename, name, newphone):
    '''Замінює у довіднику у файлі filename телефон за ім'ям name на newphone.

    Якщо не знайдено, нічого не робить.
    '''
    f = open(filename,'rb')
    book = pickle.load(f)   #завантажуємо довідник з файлу у словник book
    f.close()
    if name in book:
        book[name] = newphone   #присвоюємо новий телефон знайомому
        f = open(filename,'wb')
        pickle.dump(book,f)     #записуємо оновлений довідник у файл
        f.close()
  
    
filename = 'ref.dat'    #ім'я файлу довідника

while True:
    k = int(input('Режим роботи [1 - 5]:'))
    if k == 1:              #створити довідник
        createrb(filename)
    elif k == 2:            #додати запис до довідника
        apprb(filename)
    elif k == 3:            #знайти телефон у довіднику
        name = input('Прізвище: ')
        phone = searchrb(filename, name)
        if len(phone) > 0:
            print('Телефон:', phone)
        else:
            print('не знайдено')
    elif k == 4:            #замінити телефон у довіднику
        name = input('Прізвище: ')
        phone = input('Новий телефон: ')
        replacerb(filename, name, phone)
    elif k == 5:
        break
        





      


