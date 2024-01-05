#T29_21 Класи введення-виведення об'єктів запису на курси у БД.

import sqlite3

class CourseDB:
    """Клас з'єднання з базою даних курсів.

        self.urn - розташування БД курсів
        self.conn - об'єкт зв'язку з базою даних
    """
    def __init__(self, urn):
        self.urn = urn
        self.conn = None

    def get_cursor(self):
        "Повертає об'єкт курсор."
        self.conn = sqlite3.connect(self.urn)    # зв'язатись з БД
        return self.conn.cursor()

    def close(self):
        "Завершує з'єднання з БД."
        if self.conn:
            self.conn.commit()
            self.conn.close()
        self.conn = None

    def get_data_dicts(self, query, *param):
        """Повертає список словників з даними.

           Як відповідь на запит query з параметрами param.
        """
        curs = self.get_cursor()
        curs.execute(query, param)
        # взято з Mark Lutz - Programming Python.
        # отримати назви полів
        colnames = [desc[0] for desc in curs.description]
        # створити список словників
        rowdicts = [dict(zip(colnames, row)) for row in curs.fetchall()]
        self.close()
        return rowdicts
        

class CourseCollection:
    """Клас для отримання даних курсів.

        self.db - об'єкт БД
    """
    def __init__(self, db):
        self.db = db

    def get_courses(self):
        "Повертає список курсів."
        query = "SELECT * FROM course"
        courses = self.db.get_data_dicts(query)
        return courses

    def get_courses_authored(self, user):
        "Повертає список курсів, у яких user є автором."
        query = "SELECT * FROM course WHERE author_id=?"
        courses = self.db.get_data_dicts(query, user["id"])
        return courses

    def get_courses_applied(self, user):
        "Повертає список курсів, на які user записався."
        query = """SELECT * FROM course WHERE id IN
                     (SELECT course_id FROM student_course
                     WHERE student_id=?)"""
        courses = self.db.get_data_dicts(query, user["id"])
        return courses

    def _get_by_id(self, dict_list, _id):
        "Повертає словник - запис з даними - за значенням _id у списку dict_list."
        result = None
        ids = [d["id"] for d in dict_list]
        if _id in ids:
            pos = ids.index(_id)
            result = dict_list[pos]
        return result
        
    def _get_user_rights(self, user):
        """Повертає права користувача на кожну функцію.

          права - це словник {function1: [right1, ... , rightn], ...}
          righti - кортеж (назва права, чи застосовується тільки для автора)
        """
        # повернути назви прав
        query = "SELECT * FROM right"
        rights = self.db.get_data_dicts(query)
        # повернути функції
        query = "SELECT * FROM function"
        functions = self.db.get_data_dicts(query)
        user_rights = {func["name"]:[] for func in functions}
        query = """SELECT right_id, is_auth FROM function_right
                   WHERE role_id=? AND function_id=?"""
        for func in functions:
            # повернути права ролі на функцію
            function_rights = self.db.get_data_dicts(query,
                            user["role_id"], func["id"])
            # заповнити словник з правами
            for f_r in function_rights:
                right = self._get_by_id(rights, f_r["right_id"])
                user_rights[func["name"]].append((right["name"], f_r["is_auth"]))
        return user_rights

    def get_user(self, login, password):
        "Повертає дані користувача або {}, якщо неправильний пароль."
        user = {}
        query = "SELECT * FROM user WHERE login=? AND password=?"
        lst = self.db.get_data_dicts(query, login, password)
        if lst:
            user = lst[0]
            # повернути назву ролі
            query = "SELECT name FROM role WHERE id=?"
            roles = self.db.get_data_dicts(query, user["role_id"])
            user["role"] = roles[0]["name"]
            user["rights"] = self._get_user_rights(user)
        return user

    def get_course_by_id(self, courses, course_id):
        "Повертає курс із списку курсів за id."
        return self._get_by_id(courses, course_id)

    def create_course(self, name, description, program, user_id):
        "Створює курс за ім'ям, описом та програмою"
        curs = self.db.get_cursor()
        curs.execute("""INSERT INTO course(name, description, program, author_id)
                VALUES (?, ?, ?, ?)""", (name, description, program, user_id))
        self.db.close()
    
    def modify_course(self, name, description, program, course_id):
        "Оновлює курс course_id"
        curs = self.db.get_cursor()
        curs.execute("""UPDATE course SET name=?, description=?, program=?
                     WHERE id=?""", (name, description,
                                    program, course_id))
        self.db.close()

    def delete_course(self, course_id):
        "Видаляє курс course_id"
        curs = self.db.get_cursor()
        curs.execute("DELETE FROM student_course WHERE course_id=?",
                     (course_id, ))
        curs.execute("DELETE FROM course WHERE id=?", (course_id, ))
        self.db.close()
        

    def apply_to_course(self, user, course):
        "Записує користувача user на курс course."
        curs = self.db.get_cursor()
        curs.execute("""INSERT INTO student_course(student_id, course_id)
                     VALUES (?, ?)""", (user["id"], course["id"]))
        self.db.close()
                    
    def unapply_from_course(self, user, course):
        "Записує користувача user на курс course."
        curs = self.db.get_cursor()
        curs.execute("""DELETE FROM student_course WHERE
                  student_id=? AND course_id=?""", (user["id"], course["id"]))
        self.db.close()
                    
    
    def get_students_applied(self, course_id):
        "Повертає список студентів, які записались на курс course_id."
        query = """SELECT * FROM user WHERE id IN
                     (SELECT student_id FROM student_course
                     WHERE course_id=?)"""
        students = self.db.get_data_dicts(query, course_id)
        return students
        
