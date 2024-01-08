# t27_31_wsgi_fib_web.py
# Обчислення чисел Фібоначчі через WSGI-сервер.

import cgi

HTML_PAGE = """<html>
<title>Обчислення чисел Фібоначчі</title>
<body>
<h3>Обчислення заданого числа Фібоначчі</h3>
<br>
{}
<br>
<br>
<form method=POST action="">
<table>
<tr>
<td align=right>
<font size="5" color="blue" face="Arial">
Введіть номер числа Фібоначчі:
</font>
</td>
<td>
<input type=text name=n_val value="">
</td>
<tr>
<td colspan=2 align=center>
<input type=submit value="Обчислити">
</td>
<table>
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

def application(environ, start_response):
    """Викликається WSGI-сервером.

       Отримує оточення environ та функцію,
       яку треба викликати у відповідь: start_response.
       Повертає відповідь, яка передається клієнту.
    """
    if environ.get('PATH_INFO', '').lstrip('/') == '':
        # отримати словник параметрів, переданих з HTTP-запиту
        form = cgi.FieldStorage(fp=environ['wsgi.input'], 
                        environ=environ)
        result = ''
        if 'n_val' in form:
            n = int(form['n_val'].value)
            result = 'Fib({}) = {}'.format(n, fib(n))
        body = HTML_PAGE.format(result)
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    else:
        # якщо команда невідома, то виникла помилка
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        body = 'Сторінку не знайдено'
    return [bytes(body, encoding='utf-8')]


if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()


