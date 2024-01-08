#T22_01_v2

# Побудова списку каталогів разом з їх розмірами
# та впорядкування їх за незростанням розміру
# Перенаправлення стандарного виведення у файл

import os

def getdirsize(dir):
    '''Повертає загальний обсяг файлів у заданому каталозі dir.

    Обчислює сумарний обсяг по всіх підкаталогах.
    '''
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
    return size

def getdirslist(directory):
    '''Повертає список підкаталогів каталогу directory разом з їх обсягами.

    Список впорядковано за незростанням розміру.
    Список складається з кортежів (<розмір>, <ім'я каталогу>)
    '''
    lst = os.listdir(directory)
#    print(lst)
    dirsizelist = []
    for dir in lst:
        fullpath = os.path.join(directory, dir) # обчислюємо повний шлях
        if os.path.isdir(fullpath):
            # додаємо кортеж до списку
            dirsizelist.append((getdirsize(fullpath), fullpath))
    dirsizelist.sort(reverse=True)  # впорядковує список за незростанням
    return dirsizelist

    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        directory = input("Directory name: ")
    else:
        directory = sys.argv[1]
    newout = open('dirslist.txt', 'w')
    oldout = sys.stdout
    sys.stdout = newout         # перенаправлення стандарного виведення
    dirsizelist = getdirslist(directory)
    for item in dirsizelist:
        print('{:40} size: {:>20,}'.format(item[1], item[0]))
    sys.stdout = oldout         # повернення попереднього стандартного виведення
    newout.close()

