#T26_11 Завантаження файлу з Інтернет

import sys
import os
from urllib.request import urlretrieve

if len(sys.argv) == 1:
    filename = input('Filename:')
    theme_no = input('Theme number:')
else:
    filename = sys.argv[1]
    theme_no = sys.argv[2]

url = 'http://matfiz.univ.kiev.ua/userfiles/files/Pres{}.pdf'.format(theme_no)
#print(url)

result = urlretrieve(url, filename) # завантажуємо файл
print(result[0], result[1], sep='\n')

os.startfile(filename)              # запускаємо Adobe Reader

