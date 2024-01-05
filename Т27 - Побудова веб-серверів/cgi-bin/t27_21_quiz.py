#T27_21 Класи опису тестів.

import datetime
from collections import namedtuple

# Типи питань
YESNO   = "yesno"   # так або ні
ONLYONE = "onlyone" # з одним варіантом
SEVERAL = "several" # з декількома варіантами

# Кортеж для відповіді питання тесту
# (питання, текст, очікуване_значення_відповіді)
Answer = namedtuple("Answer", ["master", "text", "value"])
# Кортеж для результату тесту
# (користувач, дата_час, тест, бали, максимально_можливі_бали)
Result = namedtuple("Result",
                    ["user", "when", "quiz", "points", "maxpoints"])
                    

class QuizSuite:
    """Клас реалізує набір тестів.

       self.IO - об'єкт класу введення тестів та виведення результатів
       self.quizzes - список тестів (об'єктів класу Quiz)
       self.results - список результатів (кортежів Result)
    """

    def __init__(self, testIOclass, urn, **params):
        """Конструктор.

           testIOclass - клас введення тестів та виведення результатів,
           urn - розташування ресурсу з тестами (файл або база даних),
           params - додаткові параметри для читання тестів
        """
        self.IO = testIOclass(self, urn, **params)
        self.quizzes = self.IO.read()

    def __str__(self):
        """Повернути представлення у вигляді рядка."""
        return "QuizSuite({})".format(self.quizzes)

    def getthemes(self):
        """Повернути список тем (назв) тестів."""
        themes = []
        for quiz in self.quizzes:
            themes.append(quiz.text)
        return themes

    def getusers(self):
        """Повернути список користувачів."""
        return self.IO.users

    def getquiz(self, theme):
        """Повернути об'єкт тесту."""
        for quiz in self.quizzes:
            if quiz.text == theme: break
        else:
            raise ValueError(theme)
        return quiz

    def writeresult(self, result):
        """Додати до списку результатів результат (result) тесту."""
        self.IO.writeresult(result)
    

class Quiz:
    """Клас реалізує один тест.

        self.master - набір тестів (об'єкт)
        self.text - назва тесту
        self.questions - список запитань тесту (об'єктів класу Question)
    """

    def __init__(self, master, theme):
        self.master = master
        self.text = theme
        self.questions = []

    def __str__(self):
        """Повернути представлення у вигляді рядка."""
        return "Quiz({})".format(self.text)

    def assess(self, user, replies):
        """Оцінити тест та повернути результат (кортеж Result).

           replies - список списків вибраних відповідей на запитання.
           Кожна відповідь - список значень (True - вибрано або False)
           для кожного варіанту відповіді
        """
        points = 0      # кількість балів
        maxpoints = 0   # максимальна кількість балів
        # поточна дата та час
        dt = datetime.datetime.now()
        when = dt.strftime("%d.%m.%Y %H:%M")
        for i, question in enumerate(self.questions):
            reply = replies[i]
            points += question.assess(reply)
            maxpoints += question.points
        return Result(user, when, self.text, points, maxpoints)
        
    def writeresult(self, result):
        """Додати до списку результатів результат (result) тесту."""
        self.master.writeresult(result)
        
class Question:
    """Клас реалізує одне питання тесту.

        self.master - тест (об'єкт)
        self.text - текст питання
        self.type - тип питання (так/ні - YESNO,
                з одним варіантом - ONLYONE,
                з декількома варіантами - SEVERAL)
        self.points - кількість балів за питання
        self.answers - список запитань тесту (кортежів Answer)
    """

    def __init__(self, master, text, typ, points):
        self.master = master
        self.text = text
        self.type = typ
        self.points = points
        self.answers = []

    def __str__(self):
        """Повернути представлення у вигляді рядка."""
        return "Question({} {} {})".format(self.text, self.type, self.points)

    def assess(self, reply):
        """Оцінити питання та повернути набрану кількість балів.

           reply - список вибраних відповідей на запитання, тобто
                   список значень (True - вибрано або False)
                   для кожного варіанту відповіді
        """
        points = 0
        for j, answer in enumerate(self.answers):
            # відповідь не дорівнює закладеній у тесті
            if answer.value and not reply[j] or not answer.value and reply[j]:
                break
        else:
            points += self.points
        return points

        

