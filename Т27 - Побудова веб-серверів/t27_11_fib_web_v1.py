#!/usr/bin/env python3
# t27_11_fib_web_v1.py
# Обчислення чисел Фібоначчі через веб-сервер.

import cgi

HTML_PAGE = """Content-type: text/html; charset='utf-8'\n\n
<html>
<title>Fibonacci calculation</title>
<body>
<h3>Calculate given Fibonacci number</h3>
<br>
{}
<br>
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

print(HTML_PAGE.format(result))

