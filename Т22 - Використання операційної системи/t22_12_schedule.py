#T22_12
# Запуск програми збереження файлів з заданих каталогів (backup) за графіком
# Параметри отримуються з конфігураційного файлу

import os
import datetime
import logging
from time import sleep
from T21.t21_21_config_dict import *

LOGFILENAME = 'backup.log'              #ім'я файлу журналу
FORMAT = '%(asctime) -15s %(message)s'  #формат запису: <час> <повідомлення>
logging.basicConfig(filename = LOGFILENAME, format=FORMAT, level = logging.DEBUG)


def backupneeded(backupdir, interval):
    '''Перевіряє, чи потрібно виконувати backup у каталозі backupdir.

       interval - інтервал backup у годинах.
    '''
    backupdir = os.path.normpath(backupdir)   # отримуємо повний шлях шляхи до каталогу  
    lst = os.listdir(backupdir)               # отримуємо вміст вихідного каталогу
    dt = datetime.datetime.now()              # поточний час
    delta = datetime.timedelta(hours = interval) # різниця у часі у форматі дати/часу
    needed = True
    for item in lst:
        fullitem = os.path.join(backupdir, item) # повний шлях до елементу каталогу
        # отримати час зміни елемента каталогу
        itemtime = datetime.datetime.fromtimestamp(os.path.getmtime(fullitem))
#        print(fullitem, itemtime)
        if itemtime + delta > dt:
            needed = False
            break
    return needed


def backup(params):
    '''Виконує backup файлів згідно параметрів params.

       params - це словник, що містить параметри:
           BackupDirectory - каталог для backup
           Directories - каталоги, які треба зберігати (рядок через ' ')
           Interval - інтервал між запусками backup (годин)
       Запускає окремий процес, читає результат та зберігає у журналі backup.log    
    '''
    interval = params['Interval']
    backupdir = params['BackupDirectory']
    directories = params['Directories']
    sleeptime = int(interval * 3600) // 2  # секунди для переривання процесу
    while True:
        if backupneeded(backupdir, interval):
            logging.info('Starting backup to {} from {}'.format(backupdir,
                                                                directories))
            # запустити backup
            backupproc = 't22_11_backup_v3.py'
            rez = os.popen('{} {} {}'.format(backupproc, backupdir,
                                            directories))
            for line in rez:
                # вивести у журнал результати
                logging.info(line[:-1])
        sleep(sleeptime)

 
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:              # якщо немає параметрів, ставимо ім'я за угодою
        config = "config.txt"
    else:
        config = sys.argv[1]         # 1 параметр
    conf = ConfigDict(config)
    params = conf.getconfig()
    backup(params)
        

