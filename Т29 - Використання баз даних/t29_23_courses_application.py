#t29_23_courses_application.py
#Клас application. Реалізація запису на курси.

import cgi
import os
from t29_21_courses_db_io import *
from t29_22_courses_iface import *

MAX_APPLY = 2    # максимальна кількість курсів для запису

class CoursesSession:
    "Клас реалізує один сеанс запису на курси."
    def __init__(self, app, sid, user):
        self.app = app      # клас, що містить даний (CoursesApplication)
        self.sid = sid      # номер сесії
        self.user = user    # користувач
    

class CoursesApplication:
    """Клас реалізує взаємодію з клієнтом під час запису на курси.

        self.last_id - номер останньої започаткованої сесії
        self.sessions - словник сесій (об'єктів класу QuizSession)
        self.сс - клас взаємодії з БД
        self.iface - клас інтерфейсу користувача
        self.path - шлях до поточного каталогу від wsgi-сервера
    """
    
    def __init__(self, urn, path):
        db = CourseDB(urn)
        self.cc = CourseCollection(db)
        self.path = path + os.sep
        self.iface = CoursesInterface(self.path)
        self.last_id = 0
        self.sessions = {}

    def __call__(self, environ, start_response):
        """Викликається WSGI-сервером.

           Отримує оточення environ та функцію,
           яку треба викликати у відповідь: start_response.
           Повертає відповідь, яка передається клієнту.
        """
        command = environ.get('PATH_INFO', '').lstrip('/')
        # отримати словник параметрів, переданих з HTTP-запиту
        form = cgi.FieldStorage(fp=environ['wsgi.input'], 
                        environ=environ)
        err = False
        if command == "":
            command = "start"
        # замінити у команді '/' на '_'
        command = command.replace('/', '_')
        # отримати метод за ім'ям команди
        command_meth = getattr(self, command, None)
        if command_meth:
            # виконати команду та отримати тіло відповіді
            body = command_meth(form)
            if body:
                start_response('200 OK', [('Content-Type',
                                           'text/html; charset=utf-8')])
            else:
                # якщо body - порожній рядок, то виникла помилка
                err = True
        else:
            # якщо команда невідома, то виникла помилка
            err = True
        if err:
            start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
            body = 'Сторінку не знайдено'
        return [bytes(body, encoding='utf-8')]

    def start(self, form):
        """Обробити команду початку роботи (/).

           Спрямувати клієнту сторінку входу до системи.
        """
        body = self.iface.start()
        return body

    def _start_session(self, form):
        "Отримати дані користувача та розпочати сесію."
        # отримати з форми логін та пароль
        login = form.getfirst("login","")
        password = form.getfirst("pass","")
        user = self.cc.get_user(login, password)
        # чи правильний логін,пароль
        if user:
            success = True
            # розпочати нову сесію для користувача
            self.last_id += 1
            self.sessions[self.last_id] = CoursesSession(self,
                                                        self.last_id, user)
        else:
            success = False
        return success

    def course(self, form):
        "Спрямувати клієнту сторінку курсів."
        # якщо сторінка відкривається після login
        if not "sid" in form:
            success = self._start_session(form)
            sid = self.last_id
        else:
            success = True
            sid = int(form.getfirst("sid","0"))         # номер сесії
        if success:
            # показати курси
            ses = self.sessions[sid]
            rights = ses.user["rights"]["course"]
            courses = self.cc.get_courses()
            courses_authored = self.cc.get_courses_authored(ses.user)
            courses_applied = self.cc.get_courses_applied(ses.user)
            body = self.iface.courses_page(sid, ses.user["id"], rights,
                                    MAX_APPLY, courses,
                                    courses_authored, courses_applied)
        else:
            # показати повідомлення про помилку
            body = self.iface.login_error()
        return body
        

    def course_create(self, form):
        "Спрямувати клієнту сторінку створення курсу."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        body = self.iface.course_create_modify_page(sid)
        return body

    def course_created(self, form):
        "Додати створений курс до БД."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        if "save" in form: # якщо було натиснуто кнопку "Зберегти"
            name = form.getfirst("name","")
            description = form.getfirst("description","")
            program = form.getfirst("program","")
            ses = self.sessions[sid]
            self.cc.create_course(name, description, program, ses.user["id"])
        return self.course(form)

    def course_modify(self, form):
        "Спрямувати клієнту сторінку зміни курсу."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        course_id = int(form.getfirst("courseid","0"))
        courses = self.cc.get_courses()
        course = self.cc.get_course_by_id(courses, course_id)
        body = self.iface.course_create_modify_page(sid, course)
        return body

    def course_modified(self, form):
        "Змінити курс у БД."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        if "save" in form:  # якщо було натиснуто кнопку "Зберегти"
            course_id = int(form.getfirst("courseid","0"))
            name = form.getfirst("name","")
            description = form.getfirst("description","")
            program = form.getfirst("program","")
            ses = self.sessions[sid]
            self.cc.modify_course(name, description, program, course_id)
        return self.course(form)

    def course_delete(self, form):
        "Видалити курс у БД."
        course_id = int(form.getfirst("courseid","0"))
        self.cc.delete_course(course_id)
        return self.course(form)

    def course_view(self, form):
        "Спрямувати клієнту сторінку перегляду курсу."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        course_id = int(form.getfirst("courseid","0"))
        courses = self.cc.get_courses()
        course = self.cc.get_course_by_id(courses, course_id)
        body = self.iface.course_view_page(sid, course)
        return body

    def course_list(self, form):
        "Спрямувати клієнту сторінку списку студентів по курсу."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        course_id = int(form.getfirst("courseid","0"))
        courses = self.cc.get_courses()
        course = self.cc.get_course_by_id(courses, course_id)
        students = self.cc.get_students_applied(course_id)
        body = self.iface.course_list_page(sid, course, students)
        return body

    def course_apply(self, form):
        "Записати студента на курс."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        course_id = int(form.getfirst("courseid","0"))
        ses = self.sessions[sid]
        courses = self.cc.get_courses()
        course = self.cc.get_course_by_id(courses, course_id)
        self.cc.apply_to_course(ses.user, course)
        return self.course(form)
        
    def course_unapply(self, form):
        "Відписати студента від курсу."
        sid = int(form.getfirst("sid","0"))         # номер сесії
        course_id = int(form.getfirst("courseid","0"))
        ses = self.sessions[sid]
        courses = self.cc.get_courses()
        course = self.cc.get_course_by_id(courses, course_id)
        self.cc.unapply_from_course(ses.user, course)
        return self.course(form)


        
    
