#T13_01
#Нарахування стипендії

class Person:                       #Клас Особа
    def __init__(self):
        self.name = None            #прізвище
        self.byear = None           #рік народження

    def input(self):                #ввести особу
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):                #вивести особу
        print(self.name, self.byear, end = ' ')

class Student(Person):              #Клас Студент
    def __init__(self):
        Person.__init__(self)
        self.course = None          #курс навчання
        self.session = []           #список оцінок у сесію


    def input(self):                #ввести студента
        Person.input(self)
        self.course = int(input('Курс: '))
        self.session = []
        n = int(input('К-ть оцінок: '))
        for i in range(n):
            m = int(input('Оцінка '+str(i+1)+': '))
            self.session.append(m)

    def print(self):               #вивести студента 
        Person.print(self)
        print(self.course, self.session, end = ' ')

    def average(self):             #обчислити середнє значення оцінок у сесію 
        s = sum(self.session)
        n = len(self.session)
        if 2 in self.session or 0 in self.session:
            s = 0
        if n != 0:
            s /= n
        return s

#Завершено опис та реалізацію класів

def stip(a):
    coeff = [0.0, 1.0, 1.2] #коефіцієнти нарахування
    ball = [0.0, 4.0, 5.0]  #бали, що відповідають коефіцієнтам
    minfee = 720            #мінімальна стипендія
    i = len(ball)-1
    while ball[i] > a:
        i = i-1
    return minfee*coeff[i]

stud = []                   #список студентів (об'єктів класу Student)
n = int(input('К-ть студентів: '))
for i in range(n):
    print('Студент', i+1)
    s = Student()
    s.input()
    stud.append(s)

print('Нарахована стипендія')
for s in stud:
    a = s.average()
    st = stip(a)
    s.print()
    print(st)


