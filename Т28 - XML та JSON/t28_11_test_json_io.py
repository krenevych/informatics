#T28_11 Клас введення-виведення тестів у файли JSON.

import sys
import json

if '../T27/cgi-bin' not in sys.path:
    sys.path.append('../T27/cgi-bin')

from t27_22_testio import *
from t27_21_quiz import *

USERS_URN = "users.json"

class TestJSONIO(TestIO):
    """Клас введення тестів з файлу JSON та виведення результатів.

        self.quissuite - тести (об'єкт класу QuisSuite)
        self.urn - розташування ресурсу з тестами (файл JSON)
        self.users - список користувачів - списків [користувач, пароль]
    """

    def __init__(self, quissuite, urn):
        TestIO.__init__(self, quissuite, urn)
        # прочитати користувачів
        self._users = self._readusers()
#        print(self._users)

    def _readusers(self):
        "Повертає список користувачів."
        cnt = []
        with open(USERS_URN, 'r') as f:
            u_list = json.load(f)
        for u_dict in u_list:
               cnt.append([u_dict['user'], u_dict['password']])
        return cnt
            
        
    def read(self):
        """Читати тести.
           Повертає список об'єктів класу Quiz"""
        quizzes = []
        with open(self.urn, 'r', encoding='utf-8') as f:
            q_list = json.load(f)
        for q in q_list:
            quizzes.append(self._readquiz(q))
        return quizzes
                
    def _readquiz(self, quiz_dict):
        "Повертає тест з словника - частини json."
        theme = quiz_dict["quiz"]
        quiz = Quiz(self.quissuite, theme)
        quest_list = quiz_dict["questions"]
        for q in quest_list:
            typ = q["type"]
            points =  q["points"]
            name = q["question"]
            quest = Question(quiz, name, typ, points)
            ans_list = q["answers"]
            for a in ans_list:
                atext = a["answer"]
                avalue = bool(a["value"])
                quest.answers.append(Answer(quest, atext, avalue))
            quiz.questions.append(quest)
        return quiz

    @property
    def users(self):
        "Повертає список кортежів (користувач, пароль)"
        return self._users


    def writeresult(self, result):
        "Писати результат тесту з result."
        res_dict = {}
        res_dict["user"] = result.user
        res_dict["when"] = result.when
        when = result.when.replace(':','_')
        print(when)
        res_dict["quiz"] = result.quiz
        res_dict["points"] = result.points
        res_dict["maxpoints"] = result.maxpoints
        fname = "{0}_{1}.json".format(result.user, when)
        with open(fname, 'w') as f:
            json.dump(res_dict, f, indent=4, sort_keys=True, ensure_ascii=False)
            
if __name__ == '__main__':
    filename = input("файл: ")
    suite = QuizSuite(TestJSONIO, filename)
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
        


        

