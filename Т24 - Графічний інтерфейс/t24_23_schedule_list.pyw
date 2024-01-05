#T22_13
# Запуск програми збереження файлів з заданих каталогів (backup) за графіком
# Параметри отримуються з конфігураційного файлу
# Параметри редагуються у графічному режимі та зберігаються у тому ж файлі

from T22.t22_12_schedule import *
from t24_12_config_set import *
from t24_22_backup_gui import *

from tkinter import Tk
import sys

if len(sys.argv) == 1:              # якщо немає параметрів, ставимо ім'я за угодою
    config = "config.txt"
else:
    config = sys.argv[1]            # 1 параметр

conf = ConfigDictSet(config)
params = conf.getconfig()           # отримати параметри конфігураційного файлу
top = Tk()                          # створення вікна
bg = BackupGUI(top, params)        # створити об'єкт BackupGUI
top.mainloop()

edited = bg.get()            # отримати значення словника
if edited:
    conf.setconfig(edited)       # змінити параметри у файлі конфігурації
    conf.saveconfig()
    params = conf.getconfig()    # повторно отримуємо парамтери після зміни

    backup(params)               # запустити backup

