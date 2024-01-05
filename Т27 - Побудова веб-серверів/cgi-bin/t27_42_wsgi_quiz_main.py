#T27_42 Головний модуль проходження тестів через wsgi.

import cgi
import os
from t27_41_wsgi_quiz_application import *



PATH = '.'
URN = "quizsuite1.xlsx"


application = QuizApplication(TestExcelIO, URN, PATH)


if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()

