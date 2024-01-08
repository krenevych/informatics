#!/usr/bin/env python3
# t27_11_fib_web_v2.py
# Обчислення чисел Фібоначчі через веб-сервер.
# Формування єдиної сторінки для введення та результату.

import cgi
import os
import sys
import codecs

encoding = 'windows-1251' if os.name == 'nt' else 'utf-8'
if os.name == 'nt' and sys.stdout.encoding != 'windows-1251':
    sys.stdout = codecs.getwriter('windows-1251')(sys.stdout.buffer, 'strict')

HTML_PAGE = """Content-type: text/html; charset={}\n\n
<html>
<title>Обчислення чисел Фібоначчі</title>
<body>
<h3>Обчислення заданого числа Фібоначчі</h3>
<br>
{}
<br>
<form method=POST action="http://localhost:8000/cgi-bin/t27_11_fib_web_v2.py">
<p>Введіть номер числа Фібоначчі:
<input type=text name=n_val value="">
<input type=submit value="Обчислити">
</p>
</form>
</body>
</html>
"""

def fib(n):
    """Обчислює n-те число Фібоначчі."""
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

result = ''

form = cgi.FieldStorage()
if 'n_val' in form:
    n = int(form['n_val'].value)
    result = 'Fib({}) = {}'.format(n, fib(n))

print(HTML_PAGE.format(encoding, result))
