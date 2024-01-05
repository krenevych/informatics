# T26_21_v2 Виконання запиту POST
# Запит наявності літератури у бібліотеці університету

import sys
from t26_01_get_url_v2 import *
from urllib.request import urlopen
from urllib.parse import urlencode

if len(sys.argv) == 1:
    title = input('Title: ')
    author = input('Author: ')
else:
    title = sys.argv[1]
    author = sys.argv[1]

url = 'http://ecatalog.univ.kiev.ua'
http_file = urlopen(url)
enc = getencoding(http_file)    # отримати кодування
print(enc)

params = {'title': title, 'author': author}
query = urlencode(params, encoding=enc) # формування рядка параметрів запиту

url = 'http://ecatalog.univ.kiev.ua/ukr/elcat/new/result.php3'
#print(url)

request = urlopen(url, bytes(query, encoding=enc))# відправка запиту

# читання сторінки відповіді сервера
data = str(request.read(), encoding = enc, errors='ignore')
'''
for line in request:
    s = str(line, encoding = enc, errors='ignore')
    print(s, end='')
'''
# запис сторінки у локальний файл
with open(title + '.html', 'w') as fout:
    fout.write(data)
