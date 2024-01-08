#T21_21
#Виділення токенів (символів) з конфігураційного файлу

import re
from collections import namedtuple

P_NAME = r'(?P<NAME>[A-Za-zА-ЯҐЄІЇа-яґєії_]\w*)'# шаблон для імені
P_EQ = r'(?P<EQ>=)'                     # шаблон для знаку 'дорівнює'
P_NUM_INT = r'(?P<NUM_INT>[+-]?\d+)'    # шаблон для цілого числа
P_NUM_FLOAT = r'(?P<NUM_FLOAT>[+-]?\d+\.\d+)'   # шаблон для дійсного числа
P_STRING = r'''(?P<STRING>(?:'[^']*')|(?:"[^"]*"))''' # шаблон для рядка
P_WS = r'(?P<WS>[ \t]+)'                # шаблон для пропусків
P_COMMENT = r'(?P<COMMENT>#.*)'         # шаблон для коментарів
P_EOL = r'(?P<EOL>[\n])'                # шаблон для кінця рядка файлу
P_OTHER = r'(?P<OTHER>.+)'              # шаблон для інших (помилкових символів)


# об'єднаний шаблон для конфігураційного файлу
P_CONFIG = '|'.join([P_NAME, P_EQ, P_NUM_FLOAT, P_NUM_INT, P_STRING,
                     P_WS, P_COMMENT, P_EOL, P_OTHER])

# Словник допустимих пар токенів.
# Для кожного токену задано множину допустимих типів наступного токену
VALID_PAIRS = {'NAME': {'EQ'},
               'EQ': {'NUM_INT', 'NUM_FLOAT', 'STRING'},
               'NUM_INT': {'EOL'},
               'NUM_FLOAT': {'EOL'},
               'STRING': {'EOL'},
               'EOL': {'NAME', 'EOL'},
               'OTHER': set()}

# множина токенів, які генератор не повертає (пропускає)
SKIP = {'WS', 'COMMENT'}

# токени типів значень файлу конфігурації
VALUE_TYPES = {'NUM_INT', 'NUM_FLOAT', 'STRING'}

p_config = re.compile(P_CONFIG) # попередньо компілюємо шаблон

Token = namedtuple('Token', ['type', 'value'])

def token_generator(text):
    '''Генерує та повертає токени з тексту text.

    Токени задані шаблоном p_config.
    Генератор пропускає токени, що містяться у множині SKIP.
    '''
    for m in p_config.finditer(text):
        typ = m.lastgroup
        if typ not in SKIP:
            tok = Token(typ, m.group(typ))
#            print(tok)
            yield tok


class ConfigDict:
    '''Клас формує та повертає словник, що містить імена та значення,

    вказані у конфігураційному файлі.
    Конфігураційний файл - це текстовий файл, рядки якого мають вигляд:
    <ім'я> = <значення>
    ім'я - це ідентифікатор
    значення може бути цілим або дійсним числом, або рядком.
    Цілі та дійсні числа задаються як звичайно. Рядки беруться у апострофи (')
    або подвійні лапки (").
    Допускаються коментарі (починаються символом '#') та порожні рядки.
    '''

    def __init__(self, filename, default_dict = {}):
        '''Конструктор з параметрами

        filename - ім'я конфігураційного файлу
        default_dict - словник, що містить значення за угодою
        '''
        with open(filename, 'r') as f:  #відкриваємо файл filename
            self._text = f.read()       # читаємо весь вміст файлу
 #       print(self._text)
        self._filename = filename
        self._tokens = token_generator(self._text)  # запускаємо генератор токенів
        self._dct = default_dict                    # словник імен та значень виразів
        self._lastname = ''         # ім'я, для якого у словнику з'явиться запис
        self._tok = None            # поточний токен
        self._nexttok = Token('EOL', '') # наступний токен
        self._processed = False     # чи оброблено файл

    def _check_syntax(self):
        '''Перевірити синтаксис.

        Перевіряє, чи допустима пара токенів (та окремий токен)  
        '''
        if self._nexttok.type not in VALID_PAIRS[self._tok.type]:
            raise SyntaxError(str(self._tok) + str(self._nexttok))

    def getconfig(self):
        '''Повернути словник з даними конфігураційного файлу.

        Повертає словник з ключами - іменами та зі значеннями параметрів
        з конфігураційного файлу.
        Цілі та дійсні значення повертаються у числовому форматі.
        '''
        if not self._processed:     # якщо файл ще не оброблено
            while True:
                try:
                    # отримати наступний токен від генератора
                    self._tok, self._nexttok = self._nexttok, next(self._tokens)
                except StopIteration:
                    break
                self._check_syntax()
                typ = self._nexttok.type
                if typ == 'NAME':
                    self._lastname = self._nexttok.value
                elif typ in VALUE_TYPES:
                    if typ == 'NUM_INT':
                        val = int(self._nexttok.value)
                    elif typ == 'NUM_FLOAT':
                        val = float(self._nexttok.value)
                    elif typ == 'STRING':
                        # видалити з рядка символи ' (або ")
                        val = self._nexttok.value[1:-1]
                    self._dct[self._lastname] = val
            self._processed = True # запам'ятати, що файл вже оброблено

        return self._dct
                    

if __name__ == '__main__':
    filename = input("Ім'я файлу: ")
    conf = ConfigDict(filename)
    print('\n\n', conf.getconfig())



