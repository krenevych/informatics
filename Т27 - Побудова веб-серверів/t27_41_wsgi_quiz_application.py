#t27_41_wsgi_quiz_application.py
#Реалізація проходження тестів через wsgi.

import cgi
import os
from t27_21_quiz import QuizSuite, YESNO, ONLYONE, SEVERAL

HTML_WRONG_PASS = """

<p align=center>
	<font size="4" color="red">

		Неправилний логін/пароль. Повторіть введення
	</font>
</p>
"""


HTML_THEME = """
<tr>
        <td>
                <input type=radio name=theme value="{0}">
        </td>
        <td align=left> 
                <font size="4">
                        {1}
                </font>
        </td>

"""

HTML_CHECK = """
<tr>
        <td>
                <input type=checkbox name=answer value="{0}">
        </td>
        <td align=left> 
                <font size="4">
                        {1}
                </font>
        </td>

"""


HTML_RADIO = """
<tr>
        <td>
                <input type=radio name=answer value="{0}">
        </td>
        <td align=left> 
                <font size="4">
                        {1}
                </font>
        </td>

"""


URN = "quizsuite1.xlsx"
LOGIN_HTML_FILE = "../w_quiz_login.html"
THEMES_HTML_FILE = "../w_quiz_themes.html"
QUEST_HTML_FILE = "../w_quiz_question.html"
RESULT_HTML_FILE = "../quiz_result.html"


class QuizSession:
    "Клас реалізує одну сесію проходження тестів."
    def __init__(self, app, sid, user):
        self.app = app      # клас, що містить даний (QuizApplication)
        self.sid = sid      # номер сесії
        self.user = user    # користувач, який проходить тест
        self.replies = []   # список списків наданих відповідей
        self.quest_no = 0   # номер питання
        self.theme = ""     # тема тесту
        self.quiz = None    # тест
    

class QuizApplication:
    """Клас реалізує взаємодію з клієнтом під час проходження тестів.

        self.last_id - номер останньої започаткованої сесії
        self.sessions - словник сесій (об'єктів класу QuizSession)
        self.suite - набір тестів
        self.commands - словник команд з HTML-файлів та функцій їх обробки
    """
    
    def __init__(self, test_io_cls, urn, path, **params):
        self.path = path + os.sep
        self.last_id = 0
        self.sessions = {}
        self.suite = QuizSuite(test_io_cls, urn, **params)
        self.commands = {"": self.start,
                         "login": self.login,
                         "theme": self.theme,
                         "question": self.question}

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
        if command in self.commands:
            # виконати команду та отримати тіло відповіді
            body = self.commands[command](form)
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
            start_response('404 NOT FOUND', [('Content-Type',
                                              'text/plain; charset=utf-8')])
            body = 'Сторінку не знайдено'
        return [bytes(body, encoding='utf-8')]

    def start(self, form):
        """Обробити команду початку роботи (/).

           Спрямувати клієнту сторінку входу до системи.
        """
        with open(self.path + LOGIN_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл
            cnt = f.read()
        return cnt


    def login(self, form):
        """Обробити команду входу до системи (/login).

           Спрямувати клієнту сторінку вибору теми.
        """
        # отримати з форми логін та пароль
        login = form.getfirst("login","")
        password = form.getfirst("pass","")
        users = self.suite.getusers()
        # чи правильний логін,пароль
        if self._check_user(login, password, users):
            # розпочати нову сесію для користувача
            self.last_id += 1
            self.sessions[self.last_id] = QuizSession(self, self.last_id, login)
            # показати теми
            body = self._show_themes(self.suite.getthemes(), self.last_id)
        else:
            # показати повідомлення про помилку
            body = self._show_error()
        return body
        

    def _check_user(self, login, password, users):
        """Аутентифікація користувача."""
        success = False
        for user in users:
            # user - список [логін, пароль]
            if user == list((login, password)):
                success = True
                break
        return success

    def _show_themes(self, themes, sid):
        """Сформувати сторінку з темами тесту."""
        ins = ""
        for i, theme in enumerate(themes):
            # побудувати рядок з темами та радіокнопками
            ins = ins + HTML_THEME.format(i, theme)
        with open(self.path + THEMES_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл
            cnt = f.read()
        # вставити побудований рядок та номер сесії
        return cnt.format(ins, sid)
        
    def _show_error(self):
        """Сформувати сторінку у разі помилки входу."""
        # прочитати файл html як список
        # encoding='utf-8' потрібно для правильного кодування тексту
        with open(self.path + LOGIN_HTML_FILE, encoding='utf-8') as f:
            lines = f.readlines()
        # вставити повідомлення про помилку перед останніми 2 тегами файлу
        lines.insert(-2, HTML_WRONG_PASS)
        out = ''.join(lines)
        return out
    
    def theme(self, form):
        """Обробити команду вибору теми тесту (/theme).

           Спрямувати клієнту сторінку з першим питанням.
        """
        theme_no = int(form.getfirst("theme","0"))  # номер теми
        sid = int(form.getfirst("sid","0"))         # номер
        body = ''
        if sid in self.sessions:
            themes = self.suite.getthemes()
            ses = self.sessions[sid]
            ses.theme = themes[theme_no]
            ses.quiz = self.suite.getquiz(ses.theme)
            body = self._show_question(ses)
        return body
    
        
    def _show_question(self, ses):
        """Сформувати сторінку з питанням."""
        ins = ""
        quest = ses.quiz.questions[ses.quest_no]
        if quest.type == SEVERAL: # вибір декілької варіантів
            # вставляти кнопки вибору
            html = HTML_CHECK
        else:
            # вставляти радіокнопку
            html = HTML_RADIO
        for i, answer in enumerate(quest.answers):
            # побудувати рядок з відповідями
            ins = ins + html.format(i, answer.text)
        with open(self.path + QUEST_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл
            cnt = f.read()
        # вставити текст питання, побудований рядок, параметри
        return cnt.format(quest.text, ins, ses.sid)


    def question(self, form):
        """Обробити команду надання питання (/qurstion).

           Спрямувати клієнту сторінку з наступним питанням.
           Якщо питання закінчились, то порахувати та зберегти результат.
           Спрямувати клієнту сторінку з результатом тесту.
        """
        sid = int(form.getfirst("sid","0"))         # номер
        body = ''
        # якщо сесію не завершено
        if sid in self.sessions:
            ses = self.sessions[sid]
            # отримати відповіді на останні питання та додати їх
            # до списку відповідей 
            last_reply = self._get_reply(form, ses)
            ses.replies.append(last_reply)
            ses.quest_no += 1   # перейти до наступного питання
            if ses.quest_no < len(ses.quiz.questions):
                # ще є питання
                body = self._show_question(ses)
            else:
                # питання закінчились
                result = ses.quiz.assess(ses.user, ses.replies)
                ses.quiz.writeresult(result)
                body = self._show_result(result)
                # видалити заверешну сесію з словника сесій
                del self.sessions[ses.sid]
        return body

    def _show_result(self, result):
        """Сформувати сторінку з результатом."""
        with open(self.path + RESULT_HTML_FILE, encoding='utf-8') as f:
            # прочитати підготовлений html-файл
            cnt = f.read()
        # вставити отримані бали та максимальні бали
        return cnt.format(result.points, result.maxpoints, 'utf-8')

    def _get_reply(self, form, ses):
        """Отримати рядок з відповідями на питання.

           Результат - це список з нулів та одиниць.
           Кількість нулів та одиниць відповідає кількості відповідей.
           Одиниці ставляться для вибраних відповідей.
         """
        quest = ses.quiz.questions[ses.quest_no]
        if quest.type == SEVERAL: # вибір декілької варіантів
            # список вибраних номерів відповідей
            lst = form.getlist("answer")
            lst = list(map(int, lst))
        else:
            # список з однієї вибраної відповіді
            lst = [int(form.getfirst("answer", "-1"))]  

        # побудова списку нулів та одиниць
        r = [0] * len(quest.answers)
        for i in lst:
            r[i] = 1
        return r    
