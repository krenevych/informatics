# T26_21_v1 Виконання запиту GET
# Читання інформації з енциклопедії Київського університету

import sys
from t26_01_get_url_v2 import *
from urllib.request import urlopen
from urllib.parse import urlencode

if len(sys.argv) == 1:
    param_str = input('To search: ')
else:
    param_str = sys.argv[1]

url = 'http://eu.univ.kiev.ua'
http_file = urlopen(url)
enc = getencoding(http_file)            # отримати кодування
#print(enc)

params = {'q' : param_str}
query = urlencode(params, encoding=enc) # формування рядка запиту

# URL з запитом
url = 'http://eu.univ.kiev.ua/search/index.php?' + query
print(url)

request = urlopen(url)                  # відправка запиту

# читання сторінки відповіді сервера
data = str(request.read(), encoding = enc, errors='ignore')
'''
for line in request:
    s = str(line, encoding = enc, errors='ignore')
    print(s, end='')
'''
# запис сторінки у локальний файл
with open(param_str + '.html', 'w') as fout:
    fout.write(data)
