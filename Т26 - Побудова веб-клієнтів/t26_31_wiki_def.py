# T26_31 Отримання означення з вікіпедії за запитом.

import html.parser
from t26_01_get_url_v2 import *
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError



class WikiDefParser(html.parser.HTMLParser):
    '''Клас, що розбирає сторінку з Вікіпедії та формує означення.

       В якості означення береться текст у першому тезі <p> ... </p>
    '''
    def __init__(self, *args, **kwargs):
        html.parser.HTMLParser.__init__(self, *args, **kwargs)
        self.pieces = []        # список частин тексту означення
        self.in_p = False       # чи знаходимось ми усередині тегу <p>
        # self.in_p дорівнює
            # False до першого тегу <p>,
            # True всередині першого тегу <p>,
            # None після першого тегу <p>
        
    def handle_starttag(self, tag, attrs):
        '''Обробляє початковий тег tag (<p>).'''
        if tag == 'p' and self.in_p != None:
            self.in_p = True
        
    def handle_endtag(self, tag):
        '''Обробляє кінцевий тег tag (<p>).'''
        if tag == 'p':
            self.in_p = None
        
    def handle_data(self, data):
        '''Обробляє дані data.'''
        if self.in_p:
            self.pieces.append(data)

    @property
    def getdef(self):
        '''Повертає рядок означення.'''
        return ' '.join(self.pieces)


class WikiDef:
    '''Клас для читання статті Вікіпедії за запитом та повернення означення.'''
    def __init__(self, p_str, lang='uk'):
        '''Конструктор відкриває та аналізує статтю.

           p_str - рядок запиту,
           lang - мова вікіпедії (може бути ще en, ru)'''
        self._def = ''                          # означення терміну
        url = 'https://{}.wikipedia.org'.format(lang)
#        print(url)
        http_file = urlopen(url)
        enc = getencoding(http_file)            # отримати кодування
#        print(enc)

        params = {'q' : p_str}
        query = urlencode(params, encoding=enc)[2:] # формування рядка запиту

        # URL з запитом
        url = 'https://{}.wikipedia.org/wiki/{}'.format(lang, query)
#        print(url)
        try:
            request = urlopen(url)                  # відправка запиту
#            print(request.status)
            # читання сторінки відповіді сервера
            data = str(request.read(), encoding = enc, errors='ignore')
            wdp = WikiDefParser()
            wdp.feed(data)
            self._def = wdp.getdef
        except HTTPError as e:
            print(e)

    @property
    def definition(self):
        '''Властивість повертає означення.
              
           Якщо не знайдено сторінку, то порожній рядок.
        '''
        return self._def

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        param_str = input('To search: ')
    else:
        param_str = sys.argv[1]
    wd = WikiDef(param_str)
    print('Definition:', wd.definition)


        
        
