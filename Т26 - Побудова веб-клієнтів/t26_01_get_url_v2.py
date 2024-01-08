#T26_01_v2 Відкриття сторінки у Інтернет.
#Визначення коодування за допомогою заголовків

import sys
import re
from urllib.request import urlopen

P_ENC = r'\bcharset=(?P<ENC>.+)\b'

def getencoding(http_file):
    '''Отримати кодування файлу http_file з Інтернет.'''
    headers = http_file.getheaders()    # отримати заголовки файлу
#    print(headers)
    dct = dict(headers)                 # перетворити у словник
    content = dct.get('Content-Type','')# знайти 'Content-Type'
#    print(content)
    mt = re.search(P_ENC, content)      # знайти кодування (після 'charset=' )
    #print(mt.group())
    if mt:
        enc = mt.group('ENC').lower().strip() # виділити кодування 
    elif 'html' in content:
        enc = 'utf-8'
    else:
        enc = None
    return enc

if __name__ == '__main__':
    if len(sys.argv) == 1:
        url = 'http://matfiz.univ.kiev.ua/pages/13'
    else:
        url = sys.argv[1]

    http_file = urlopen(url)
    print("Status:", http_file.status)

    enc = getencoding(http_file)
    #print(enc)

    if enc:
        for line in http_file:
            s = str(line, encoding = enc)
            print(s, end='')


