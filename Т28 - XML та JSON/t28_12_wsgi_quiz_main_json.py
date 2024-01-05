#T28_12 Головний модуль проходження тестів через wsgi (JSON)

import cgi
import os
import sys

if '../T27/cgi-bin' not in sys.path:
    sys.path.append('../T27/cgi-bin')

from t27_41_wsgi_quiz_application import *
from t28_11_test_json_io import *

PATH = '../T27/cgi-bin'
URN = "quizsuite1.json"


application = QuizApplication(TestJSONIO, URN, PATH)


if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()

