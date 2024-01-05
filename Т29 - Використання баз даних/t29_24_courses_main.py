#T29_23 Головний модуль запису на курси.

from t29_23_courses_application import *



PATH = '.'
URN = "courses.db"


application = CoursesApplication(URN, PATH)


if __name__ == '__main__':
    # створити та запуститити WSGI-сервер
    from wsgiref.simple_server import make_server
    print('=== Local WSGI webserver ===')
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()

