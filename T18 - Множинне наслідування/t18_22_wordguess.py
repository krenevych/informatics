#T18_22_wordguess.py
#Відгадування слів з використанням деку

from collections import deque
import random
import os


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


class WordGuessGame:
    def __init__(self, filename, guessers=None):
        self.guessers = guessers
        self._word = ""           #слово, що треба відгадати
        self._guessed = ""        #слово для показу (спочатку - '*')
        self._gameover = False
        self._makeword(filename)
    
    def _makeword(self, filename):
        '''Будує слово для відгадування word а також слово guessed з '*' такої ж довжини.

        '''
        offs = random.randrange(os.path.getsize(filename)) #знаходимо випадкове місце у файлі
        with open(filename, 'r', encoding='windows-1251') as f:
            f.seek(offs)
            words = []
            for i in range(10):                                 #читаємо 10 рядків
                s = f.readline()
                s = self._prepare_string(s)
                words += s.split()      #будуємо список слів
        del words[0]                #перше слово може бути неповним, видаляємо його
        words = [w for w in words if len(w) >= 3] # усі слова довжиною не менше 3
    #    print(words)
    #    s = "зв'язування між об'єктами та методами поняття віртуальних методів поліморфізм"
    #    words = s.split()
        i = random.randrange(len(words))    #вибираємо випадкове слово зі списку    
        self._word = words[i]
    #    print(word)
        self._guessed = "*"*len(self._word)     #заповнюємо слово для відгадування *

    def get_word(self):
        return self._word

    def get_guessed(self):
        return self._guessed

    def is_gameover(self):
        return self._gameover
		
    def _del_term (self, s, t):
        '''Видаляє з s усі символи-розділювачі, які є у рядку t.

        '''
        for c in t:
            s = s.replace(c,"")
        return s

    def _prepare_string (self, s):
        '''Готує рядок s до генерації слів.

        Видаляє з s усі символи-розділювачі та переводить рядок до нижнього регістру.
        '''
        r = self._del_term(s, '()0123456789,.!?:;-"\n')
        return r.lower()

    def guess(self):
        '''Виконує 1 спробу вгадати.

        '''
        while True:
            m = input("1 - літера, 2 - слово: ")
            if m in {"1", "2"}: break
        if m == '1':                              #літера
            while True:
                c = input('літера: ')
                if not c in self._guessed: break
                print(c,' - вже відгадано. Введіть іншу літеру')
            points = 0
            gw = ""
            for i in range(len(self._word)):  #замінюємо у guessed всі '*" у місцях входження c до word на с
                if self._word[i] == c:
                    gw = gw + c         #дописуємо символ c до слова відгадування
                    points += 1         #збільшуємо бали на 1
                else:
                    gw = gw + self._guessed[i]#дописуємо той символ який був у guessed
            self._guessed = gw
        else:                                   #слово
            w = input('слово: ')
            if w == self._word:               #слово відгадано
                points = self._guessed.count('*') #додаємо балів стільки, скільки було * 
                self._guessed = self._word
            else:                       #слово не відгадано
                points = -1             #-1 означає, що треба очистити всі бали
        self._gameover = not '*' in self._guessed   #гру закінчено, якщо у слові не залишилось *
        return points

    def play(self):
        '''Підтримує гру для одного слова.

        '''
        print('Починаємо відгадувати')
        self._gameover = False
        while not self._gameover:
            while True:
                print(self._guessed)         # показати поточний стан слова для відгадування
                g = self.guessers.popleft() # вибрати гравця з початку деку
                self.guessers.appendleft(g)  # додати гравця до початку деку
                print('Ваш хід,', g.getname())
                points = self.guess()
                if points > 0:
                    g.inc(points)
                    print('Ви заробили балів:', points)
                    if self._gameover:
                        print('Вітаємо! Ви виграли!!!')
                        g.inc(len(self._word))    # премія за відгадування слова
                elif points < 0:
                    print('На жаль, Ваші бали "згоріли"')
                    g.clear()
                else:                       # points == 0
                    print('Немає такої літери')
                if self._gameover or points <= 0: break 
            self.guessers.rotate(-1)             # перейти до наступного гравця
        print('Слово - ', self._word)


def inputguessers(guessers):
    '''Вводить гравців та записує їх у дек guessers.

    '''
    print('Введіть прізвища гравців. "" - завершення')
    while True:
        name = input('?')
        if len(name) == 0: break
        g = Guesser(name)           #створити гравця
        guessers.append(g)          #та додати до деку


def showguessers(guessers):
    '''Показує гравців та їх бали.

    '''
    for i in range(len(guessers)):
        g = guessers[0]       #отримати з деку поточного гравця
        g.show()              #показати його дані
        guessers.rotate(-1)   #перейти до наступного гравця


if __name__ == '__main__':
    guessers = deque()     #список гравців
    filename = 'text.txt'  #файл зі словами

    inputguessers(guessers)
    game = WordGuessGame(filename, guessers)
    game.play()
    print('Результати')
    showguessers(game.guessers)

