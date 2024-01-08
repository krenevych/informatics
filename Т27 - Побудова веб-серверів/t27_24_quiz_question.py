#!/usr/bin/env python3
# t27_24_quiz_question.py
# Передача питання тесту та обробка відповіді.

import cgi
import os
from t27_25_test_excel_io import TestExcelIO
from t27_21_quiz import QuizSuite, YESNO, ONLYONE, SEVERAL

import cgitb
cgitb.enable()

encoding = 'windows-1251' if os.name == 'nt' else 'utf-8'
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
QUEST_HTML_FILE = "quiz_question.html"
RESULT_HTML_FILE = "quiz_result.html"


def show_question(quiz, quest_no, theme_no, user, reply_str):
    """Показати сторінку з питанням."""
    ins = ""
    quest = quiz.questions[quest_no]
    if quest.type == SEVERAL: # вибір декілької варіантів
        # вставляти кнопки вибору
        html = HTML_CHECK
    else:
        # вставляти радіокнопку
        html = HTML_RADIO
    for i, answer in enumerate(quest.answers):
        # побудувати рядок з відповідями
        ins = ins + html.format(i, answer.text)
    with open(QUEST_HTML_FILE, encoding='utf-8') as f:
        # прочитати підготовлений html-файл
        cnt = f.read()
    # вставити текст питання, побудований рядок, параметри
    print(cnt.format(quest.text, ins, user, quest_no, theme_no, reply_str, encoding))

def show_result(result):
    """Показати сторінку з результатом."""
    with open(RESULT_HTML_FILE, encoding='utf-8') as f:
        # прочитати підготовлений html-файл
        cnt = f.read()
    # вставити отримані бали та максимальні бали
    print(cnt.format(result.points, result.maxpoints, encoding))

def get_reply(form, quiz, quest_no):
    """Отримати рядок з відповідями на питання.

       Результат - це рядок з нулів та одиниць, розділених комами.
       Кількість нулів та одиниць відповідає кількості відповідей.
       Одиниці ставляться для вибраних відповідей.
       Списки відповідей на окремі питання відділяються ";"
    """
    reply = ""
    if quest_no > 0:
        # якщо не перше питання, то вставити ";"
        reply = ";"
    quest = quiz.questions[quest_no]
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
    # перетворення списку у рядок
    reply += ",".join(map(str,r))
    return reply    
    
    
def assess(quiz, user, reply_str):
    """Оцінити результати тесту."""
    reply_lst = reply_str.split(";")
    replies = [list(map(int, x.split(","))) for x in reply_lst]
    result = quiz.assess(user, replies)
    return result
    
   
import sys
import codecs
if os.name == 'nt' and sys.stdout.encoding != 'windows-1251':
    sys.stdout = codecs.getwriter('windows-1251')(sys.stdout.buffer, 'strict')

form = cgi.FieldStorage()
# отримати з форми номер питання та номер теми, користувача, відповіді
quest_no = int(form.getfirst("quest_no","-1"))  # номер питання
theme_no = int(form.getfirst("theme","0"))      # номер теми
user = form.getfirst("user","0")                # користувач
reply_str = form.getfirst("reply_str","")       # відповіді

# створити об'єкт QuizSuite та отримати список користувачів з паролями
suite = QuizSuite(TestExcelIO, 'cgi-bin/'+URN)
themes = suite.getthemes()


# отримати тему та сам тест
theme = themes[theme_no]
quiz = suite.getquiz(theme)

quest_no += 1

if quest_no == 0:
    # перше питання: тільки сформувати html
    show_question(quiz, quest_no, theme_no, user, reply_str)
else:
    # не перше питання: отримати та записати відповіді
    last_reply = get_reply(form, quiz, quest_no - 1)
    reply_str += last_reply
    if quest_no < len(quiz.questions):
        # ще є питання
        show_question(quiz, quest_no, theme_no, user, reply_str)
    else:
        # питання закінчились
        result = assess(quiz, user, reply_str)
        quiz.writeresult(result)
        show_result(result)
    

