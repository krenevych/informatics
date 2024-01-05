#T29_22 Клас інтерфейсу курсів.

# назви кнопок
BUTTONS = {"list": "Список студентів",
           "create": "Створити курс",
           "modify": "Змінити",
           "delete" : "Видалити",
           "apply": "Записатись",
           "unapply": "Відписатись",
           "back": "Назад"
           }

BUTTONS_IN_ROW = 4  #кількість клітинок для кнопок у таблиці курсів

# кнопки у таблиці курсів
GRID_BUTTONS = ["list", "modify", "delete", "apply"]

BUTTON = '<input type=submit value="{0}">'
DISABLED_BUTTON = '<input type=submit value="{0}" disabled>'


HTML_WRONG_PASS = """

<p align=center>
	<font size="4" color="red">

		Неправилний логін/пароль. Повторіть введення
	</font>
</p>
"""

HTML_APPLIED = """
<p align=center>Максимальна кількість курсів, на яку можна записатись, - {1}<p>
<h3 align=center>Курси, на які Ви записані</h3>
<table align=center>
	<!-- Вставити курси -->
	{0}
</table>
"""

HTML_COURSE = "<tr><td>{0}</td>"
HTML_STUD = "<tr><td>{0}</td><td>{1}</td><td>{2}</td>"

LOGIN_HTML_FILE = "course_login.html"
COURSES_HTML_FILE = "courses.html"
COURSE_ROW_HTML_FILE = "course_row.html"
CREATE_HTML_FILE = "course_create.html"
VIEW_HTML_FILE = "course_view.html"
LIST_HTML_FILE = "course_list.html"


class CoursesInterface:
    """Клас реалізує інтерфейс користувача запису на курси.

        self.path - шлях до поточного каталогу від wsgi-сервера
    """
    def __init__(self, path):
        self.path = path

    def start(self):
        """Сформувати cторінку входу до системи.
        """
        with open(self.path + LOGIN_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл
            cnt = f.read()
        return cnt

    def login_error(self):
        """Сформувати сторінку у разі помилки входу."""
        # прочитати файл html як список
        with open(self.path + LOGIN_HTML_FILE, encoding='utf-8') as f:
            lines = f.readlines()
        # вставити повідомлення про помилку перед останніми 2 тегами файлу
        lines.insert(-2, HTML_WRONG_PASS)
        out = ''.join(lines)
        return out

    def _add_applied(self, courses_applied, max_apply):
        "Повернути html для курсів, на які користувач записаний."
        applied_str = ""
        for course in courses_applied:
            applied_str += HTML_COURSE.format(course["name"])
        cnt = HTML_APPLIED.format(applied_str, max_apply)
        return cnt

    def _add_course(self, course, sid, user_id, rights,
                    max_apply, courses_authored, courses_applied, row_cnt):
        "Повернути рядок таблиці html для одного курсу."
        auth_ids = [c["id"] for c in courses_authored] # id курсів автора
        apply_ids = [c["id"] for c in courses_applied] # id записаних курсів
        rights_names = [r[0] for r in rights] # назви прав
        row_buttons = [] # список рядків для вставки у html
        for but in GRID_BUTTONS:
            # якщо вже записано на курс, вставити кнопку "Відписатись"
            if but == "apply" and course["id"] in apply_ids:
                _but = "unapply"
            else:
                _but = but
            if but in rights_names:
                r_index = rights_names.index(but)
                # якщо вимагає автора та користувач не є автором
                # або користувач записаний на максимальну кількість курсів
                if rights[r_index][1] and course["id"] not in auth_ids \
                   or _but == "apply" and len(courses_applied) >= max_apply:
                    but_str = DISABLED_BUTTON.format(BUTTONS[_but])
                else:
                    but_str = BUTTON.format(BUTTONS[_but])
                # доповнити командою (правом) та кнопкою
                row_buttons.append(_but)
                row_buttons.append(but_str)
        # якщо кнопок менше макс. кількості, - доповнити порожніми рядками
        for i in range(len(row_buttons), BUTTONS_IN_ROW * 2):
                row_buttons += ["", ""]
        # список параметрів для вставки у html
        ins = [course["id"], course["name"], sid] + row_buttons
        cnt = row_cnt.format(*ins)
        return cnt


    def courses_page(self, sid, user_id, rights, max_apply, courses, 
                courses_authored, courses_applied):
        "Сформувати сторінку курсів."
        with open(self.path + COURSES_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл курсів
            cnt = f.read()
        with open(self.path + COURSE_ROW_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлену вставку - html-файл рядка курсу
            row_cnt = f.read()
        rights_names = [r[0] for r in rights] # назви прав
        # якщо користувач має право створити курс
        if "create" in rights_names:
            create_button_value = BUTTONS["create"]
            create_str = BUTTON.format(create_button_value)
        else:
            create_str = ""
        # якщо користувач має право записатись на курс
        if "apply" in rights_names:
            apply_str = self._add_applied(courses_applied, max_apply)
        else:
            apply_str = ""
        # заповнити таблицю курсів
        grid_str = ""
        for course in courses:
            course_str = self._add_course(course, sid, user_id, rights,
                                          max_apply, courses_authored,
                                          courses_applied, row_cnt)
            grid_str += course_str + '\n'
        body = cnt.format(grid_str, sid, apply_str, create_str)
        return body

    def course_create_modify_page(self, sid, course=None):
        "Сформувати сторінку створення/зміни курсу."
        with open(self.path + CREATE_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл створення/зміни курсу
            cnt = f.read()
        if not course:  # створити
            body = cnt.format("created", "", "", "", sid, "", BUTTONS["create"])
        else:   # змінити
            body = cnt.format("modified", course["name"], course["description"],
                    course["program"], sid, course["id"], BUTTONS["modify"])
        return body
    
    def course_view_page(self, sid, course):
        "Сформувати сторінку перегляду курсу."
        with open(self.path + VIEW_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл створення/зміни курсу
            cnt = f.read()
        body = cnt.format(course["name"], course["description"],
                            course["program"], sid)
        return body
    
    def course_list_page(self, sid, course, students):
        "Сформувати сторінку списку студентів курсу."
        with open(self.path + LIST_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл списку студентів курсу
            cnt = f.read()
        applied_str = ""
        for student in students:
            applied_str += HTML_STUD.format(student["surname"],
                                student["name"], student["secondname"])
        body = cnt.format(course["name"], applied_str, sid)
        return body
        


        
