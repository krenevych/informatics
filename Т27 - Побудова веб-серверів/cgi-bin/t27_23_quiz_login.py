#T27_23 Вхід до проходження тестів.

import cgi
import os
from t27_22_testio import *

import cgitb
cgitb.enable()


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

URN = "quizsuite1.xlsx"
LOGIN_HTML_FILE = "quiz_login.html"
THEMES_HTML_FILE = "quiz_themes.html"

def check_user(login, password, users):
    """Аутентифікація користувача."""
    success = False
    for user in users:
        # user - список [логін, пароль]
        if user == list((login, password)):
            success = True
            break
    return success

def show_error():
    """Показати помилку входу."""
    # прочитати файл html як список
    # encoding='utf-8' потрібно для правильного кодування тексту
    with open(LOGIN_HTML_FILE, encoding='utf-8') as f:
        lines = f.readlines()
    # вставити повідомлення про помилку перед останніми 2 тегами файлу
    lines.insert(-2, HTML_WRONG_PASS)
    out = ''.join(lines)
    print(out)
    
def show_themes(themes, user):
    """Показати сторінку з вибором теми тесту."""
    ins = ""
    for i, theme in enumerate(themes):
        # побудувати рядок з темами та радіокнопками
        ins = ins + HTML_THEME.format(i, theme)
    with open(THEMES_HTML_FILE, encoding='utf-8') as f:
        # прочитати підготовлений html-файл
        cnt = f.read()
    # вставити побудований рядок та ім'я користувача
    print(cnt.format(ins, user))
    

if __name__ == '__main__':
    form = cgi.FieldStorage()
    # отримати з форми логін та пароль
    login = form.getfirst("login","")
    password = form.getfirst("pass","")
    # створити об'єкт QuizSuite та отримати список користувачів з паролями
    suite = QuizSuite(TestExcelIO, 'cgi-bin/'+URN)
    users = suite.getusers()
    # чи правильний логін,пароль
    if check_user(login, password, users):
        # показати теми
        show_themes(suite.getthemes(), login)
    else:
        # показати повідомлення про помилку
        show_error()

