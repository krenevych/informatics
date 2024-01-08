#T14_10_wordguess.py
#Відгадування слів з використанням деку

from collections import deque
import random
import os

word = ""           #слово, що треба відгадати
guessed = ""        #слово для показу (спочатку - '*')
guessers = deque()     #список гравців
gameover = False       #ознака завершення гри
filename = 'text.txt'  #файл зі словами


class Guesser:
    '''Клас відгадувач
    '''
    def __init__(self, name):
        self._name = name           #ім"я
        self._points = 0            #бали

    def show(self):
        '''Показати результат.
        '''
        print(self._name, self._points)

    def inc(self, points):
        '''Збільшити кількість балів на points.
        '''
        self._points += points

    def clear(self):
        '''Очистити бали.
        '''
        self._points = 0

    def getname(self):
        '''Повернути ім"я гравця.
        '''
        return self._name

def del_term (s, t):
    '''Видаляє з s усі символи-розділювачі, які є у рядку t.

    '''
    for c in t:
        s = s.replace(c,"")
    return s

def prepare_string (s):
    '''Готує рядок s до генерації слів.

    Видаляє з s усі символи-розділювачі та переводить рядок до нижнього регістру.
    '''
    r = del_term(s, '()0123456789,.!?:;-"’\n')
    return r.lower()

def makeword(filename):
    '''Будує слово для відгадування word а також слово guessed з '*' такої ж довжини.

    '''
    global word, guessed
    f = open(filename, encoding='windows-1251')
    offs = random.randrange(os.path.getsize(filename)) #знаходимо випадкове місце у файлі
    f.seek(offs)
    words = []
    for i in range(10):                                 #читаємо 10 рядків
        s = f.readline()
        s = prepare_string(s)
        words += s.split()      #будуємо список слів
    del words[0]                #перше слово може бути неповним, видаляємо його
    f.close()
    words = [w for w in words if len(w) >= 3] # усі слова довжиною не менше 3
#    print(words)
#    s = "зв'язування між об'єктами та методами поняття віртуальних методів поліморфізм"
#    words = s.split()
    i = random.randrange(len(words))    #вибираємо випадкове слово зі списку    
    word = words[i]
#    print(word)
    guessed = "*"*len(word)     #заповнюємо слово для відгадування *
    return word, guessed


def inputguessers(guessers):
    '''Вводить гравців та записує їх у дек guessers.

    '''
    print('Введіть прізвища гравців. "" - завершення')
    while True:
        name = input('?')
        if len(name) == 0: break
        g = Guesser(name)           #створити гравця
        guessers.append(g)          #та додати до деку

def guess():
    '''Виконує 1 спробу вгадати.

    '''
    global word, guessed, gameover
    while True:
        m = input("1 - літера, 2 - слово: ")
        if m in {"1", "2"}: break
    if m == '1':                              #літера
        while True:
            c = input('літера: ')
            if not c in guessed: break
            print(c,' - вже відгадано. Введіть іншу літеру')
        points = 0
        gw = ""
        for i in range(len(word)):  #замінюємо у guessed всі '*" у місцях входження c до word на с
            if word[i] == c:
                gw = gw + c         #дописуємо символ c до слова відгадування
                points += 1         #збільшуємо бали на 1
            else:
                gw = gw + guessed[i]#дописуємо той символ який був у guessed
        guessed = gw
    else:                                   #слово
        w = input('слово: ')
        if w == word:               #слово відгадано
            points = guessed.count('*') #додаємо балів стільки, скільки було * 
            guessed = word
        else:                       #слово не відгадано
            points = -1             #-1 означає, що треба очистити всі бали
    gameover = not '*' in guessed   #гру закінчено, якщо у слові не залишилось *
    return points

def showguessers(guessers):
    '''Показує гравців та їх бали.

    '''
    for i in range(len(guessers)):
        g = guessers[0]       #отримати з деку поточного гравця
        g.show()              #показати його дані
        guessers.rotate(-1)   #перейти до наступного гравця

def play(guessers):
    '''Підтримує гру для одного слова.

    '''
    global guessed, gameover
    print('Починаємо відгадувати')
    gameover = False
    while not gameover:
        while True:
            print(guessed)         # показати поточний стан слова для відгадування
            g = guessers.popleft() # вибрати гравця з початку деку
            print('Ваш хід,', g.getname())
            points = guess()
            if points > 0:
                g.inc(points)
                print('Ви заробили балів:', points)
                if gameover:
                    print('Вітаємо! Ви виграли!!!')
                    g.inc(len(word))    # премія за відгадування слова
            elif points < 0:
                print('На жаль, Ваші бали "згоріли"')
                g.clear()
            else:                       # points == 0
                print('Немає такої літери')
            guessers.appendleft(g)  # додати гравця до початку деку
            if gameover or points <= 0: break 
        guessers.rotate(-1)             # перейти до наступного гравця
    print('Слово - ', word)

if __name__ == '__main__':
    makeword(filename)
    inputguessers(guessers)
    play(guessers)
    print('Результати')
    showguessers(guessers)

