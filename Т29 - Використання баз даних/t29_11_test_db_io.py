#t29_11_test_db_io.py
#Клас введення-виведення тестів у файли БД.

import sys
import sqlite3

if '../T27/cgi-bin' not in sys.path:
    sys.path.append('../T27/cgi-bin')

from t27_22_testio import *
from t27_21_quiz import *

class TestDBIO(TestIO):
    """Клас введення тестів з бази даних та виведення результатів.

        self.quissuite - тести (об'єкт класу QuisSuite)
        self.urn - розташування ресурсу з тестами (файл БД)
        self.users - список користувачів - списків [користувач, пароль]
        self.curs - об'єкт курсора БД для виконання дій над БД
    """

    def __init__(self, quissuite, urn):
        TestIO.__init__(self, quissuite, urn)
        self.curs = None
        # прочитати користувачів
        self._users = self._readusers()
#        print(self._users)

    def _readusers(self):
        "Повертає список користувачів."
        conn = sqlite3.connect(self.urn)    # зв'язатись з БД
        self.curs = conn.cursor()           # створити курсор
        # знайти та повернути усі записи
        self.curs.execute("SELECT name, password FROM user")
        result = self.curs.fetchall()
#        print(result)
        cnt = list(map(list, result)) # перетворити у список списків
#        print(cnt)
        conn.close()
        return cnt
        
    def read(self):
        """Читати тести.
           Повертає список об'єктів класу Quiz"""
        quizzes = []
        conn = sqlite3.connect(self.urn)     # зв'язатись з БД
        self.curs = conn.cursor()            # створити курсор
        # знайти та повернути усі записи
        self.curs.execute("SELECT id, theme FROM quiz")
        q_list = self.curs.fetchall()
        for q in q_list:
            quizzes.append(self._readquiz(q))
        conn.close()
        return quizzes
                
    def _readquiz(self, quiz_tuple):
        "Повертає тест з бази даних. quiz_tuple - кортеж (id, theme)"
        q_id, theme = quiz_tuple
        quiz = Quiz(self.quissuite, theme)
        # знайти та повернути усі запитання тесту
        self.curs.execute("""SELECT id, name, type, points
                          FROM question
                          WHERE quiz_id=?""", (q_id, ))
        quest_list = self.curs.fetchall()
        for q in quest_list:
            quest_id, name, typ, points = q
            quest = Question(quiz, name, typ, points)
            # знайти та повернути усі відповіді на запитання
            self.curs.execute("""SELECT name, value
                              FROM answer
                              WHERE question_id=?""", (quest_id, ))
            ans_list = self.curs.fetchall()
            for a in ans_list:
                atext = a[0]
                avalue = bool(a[1])
                quest.answers.append(Answer(quest, atext, avalue))
            quiz.questions.append(quest)
        return quiz

    @property
    def users(self):
        "Повертає список кортежів (користувач, пароль)"
        return self._users


    def writeresult(self, result):
        "Писати результат тесту з result."
        conn = sqlite3.connect(self.urn)     # зв'язатись з БД
        self.curs = conn.cursor()            # створити курсор
        # повернути id користувача
        self.curs.execute("""SELECT id FROM user
                          WHERE name=?""", (result.user, ))
        user_id = self.curs.fetchone()[0]
        # повернути id тесту
        self.curs.execute("""SELECT id FROM quiz
                          WHERE theme=?""", (result.quiz, ))
        quiz_id = self.curs.fetchone()[0]
        # записати результат
        self.curs.execute("""INSERT INTO
                          result (time, user_id, quiz_id, points, maxpoints) 
                          VALUES (?, ?, ?, ?, ?)""",
                          (result.when, user_id, quiz_id, 
                           result.points, result.maxpoints))
        conn.commit()
        conn.close()
            
if __name__ == '__main__':
    filename = input("файл: ")
    suite = QuizSuite(TestDBIO, filename)
    print(suite)
    shift = 0
    for quiz in suite.quizzes:
        print(shift*' ', quiz)
        shift += 4
        for quest in quiz.questions:
            print(shift*' ', quest)
            shift += 4
            for ans in quest.answers:
                print(shift*' ', ans)
            shift -= 4
        shift -= 4
    print(suite.getthemes())
        


        

