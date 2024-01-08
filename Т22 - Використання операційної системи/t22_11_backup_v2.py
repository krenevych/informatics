#T22_11_v2
# Збереження файлів з заданих каталогів (backup)
# Усі попередні версії backup архівуються

import os
import datetime
import tarfile

CHUNK = 1024*500    # Розмір частини файлу при копіюванні

def copyfile(filename, fromdir, todir):
    '''Копіює файл filename з каталогу  fromdir до каталогу todir.

    '''
    fromfullpath = os.path.join(fromdir, filename) # повний шлях до вихідного файлу
    tofullpath = os.path.join(todir, filename)     # повний шлях до файлу результату
    # відкриваємо файли як нетекстові, щоб копіювати будь-які файли
    fromfile = open(fromfullpath, "rb")
    tofile = open(tofullpath, "wb")
    if os.path.getsize(fromfullpath) <= CHUNK:      # якщо файл невеликий
        cnt = fromfile.read()                       # читаємо за один раз
        tofile.write(cnt)
    else:
        while True:
            cnt = fromfile.read(CHUNK)              # інакше читаємо по частинах
            if not cnt: break
            tofile.write(cnt)
    fromfile.close()
    tofile.close()

def copydir(fromdir, toparent):
    '''Копіює всі файли з каталогу  fromdir до каталогу toparent/fromdir.

       Якщо fromdir має вигляд dir1/dir2/.../dirn, то копіювання здійснюється у каталог
       toparent/dirn 
       Виконує копіювання для всіх підкаталогів fromdir рекурсивно.
       Передбачається, що каталог toparent порожній.
       Створює підкаталоги у toparent.
    '''
    fromdir = os.path.normpath(fromdir)   # отримуємо повні шляхи до каталогів  
    toparent = os.path.normpath(toparent)
    last = os.path.split(fromdir)[-1]       # last - остання частина шляху - ім'я катлогу
    curdir = os.path.join(toparent, last)
    print(curdir)
    os.mkdir(curdir)                        # створюємо підкатлог у результуючому каталозі
    lst = os.listdir(fromdir)               # отримуємо вміст вихідного каталогу
    for item in lst:
        fullitem = os.path.join(fromdir, item) # повний шлях до елементу каталогу
        if os.path.isfile(fullitem):           # якщо файл то копіюємо його
            try:
                copyfile(item, fromdir, curdir)
            except Exception as e:
                print ('copydir: skipping', item, e)  # пропускаємо файл, якщо помилка
        else:
            copydir(fullitem, curdir)       # якщо каталог, то рекурсивно викликаємо себе
            
def getbackupname(backupdir):
    '''Будує ім'я каталогу для backup у backupdir.

       Ім'я створюється як рядок поточного часу
    '''
    dt = datetime.datetime.now()
    dirname = dt.strftime('%Y%m%d_%H%M%S')  # формуємо ім'я каталогу за поточним часом
    return os.path.join(backupdir, dirname)


def removedir(dir):
    '''Видаляє всі файли та підкаталоги у dir а також сам каталог.

    '''
    dir = os.path.normpath(dir)   # отримуємо повний шлях шляхи до каталогу  
    lst = os.listdir(dir)             # отримуємо вміст каталогу
    for item in lst:
        fullitem = os.path.join(dir, item) # повний шлях до елементу каталогу
        if os.path.isfile(fullitem):       # якщо файл то видаляємо його
            try:
                os.remove(fullitem)
            except Exception as e:
                print ('removedir: skipping', item, e)  # пропускаємо файл, якщо помилка
        else:
            removedir(fullitem)       # якщо каталог, то рекурсивно викликаємо себе
    os.rmdir(dir)        # видаляємо порожній каталог   


def archivesubdirs(dir):
    '''Створює архіви підкаталогів у dir.

       Після створення архіву відповідний підкаталог видаляється
    '''
    lst = os.listdir(dir)               # отримуємо вміст каталогу
    for item in lst:
        fullitem = os.path.join(dir, item) # повний шлях до елементу каталогу
        if os.path.isdir(fullitem):        # якщо каталог то архівуємо його
            try:
                tf = tarfile.open(fullitem + '.tar.gz','w:gz')
                # відкриваємо архівний файл для запису зі стисненням у форматі gzip
                # ім'я формуємо з імені каталогу та додаємо .tar.gz
                tf.add(fullitem)
                tf.close()
                removedir(fullitem)      # видаляємо заархівований підкаталог
            except Exception as e:
                print ('archivesubdirs: skipping', item, e)  # пропускаємо підкаталог, якщо помилка

def backupdirectories(directories, backupdir):
    '''Створює backup даних з directories у backupdir.

    '''
    archivesubdirs(backupdir)        # архівуємо попередні версії
    toparent = getbackupname(backupdir)
#    print(toparent)
    os.mkdir(toparent)
    for dir in directories:
        try:
            copydir(dir, toparent)
        except Exception as e:
            print ('backupdirectories: skipping', dir, e)  # пропускаємо каталог, якщо помилка


 
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:              # якщо не вистачає параметрів, ввести
        backupdir = input("Backup directory: ")
        directories = input("Directories to backup: ").split()
    else:
        backupdir = sys.argv[1]         # 1 параметр
        directories = sys.argv[2:]      # параметри, починаючи з 2
    backupdirectories(directories, backupdir)
        

