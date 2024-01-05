# t25_11 Сервер гри у відгадування слів
# Використано приклад PythonChatServer
# з книги Beginning Python, автори Peter Norton, Alex Samuel,
# David Aitel та інші

import socketserver
import socket
import os
from T14.t14s2_12_wordguess import *

TURN = '/turn'   # команда "зробити хід"
QUIT = '/quit'   # команда "завершити"
NUM_TO_START = 3 # кількість гравців для початку гри

class ClientError(Exception):
    "Виключення у разі отримання неправильних даних від клієнта."
    pass


class NetGuesser(Guesser):
    """Відгадувач у мережі """
    def __init__(self, name, wfile):
        Guesser.__init__(self, name)
        self.wfile = wfile # файлоподібний об'єкт для передачі даних у мережі

    def __str__(self):
        return '{} {}'.format(self._name, self._points)


class WordGuessServer(socketserver.ThreadingTCPServer):
    "Клас багатопоточного TCP-сервера."

    def __init__(self, server_address, RequestHandlerClass):
        """Сервер, що ідтримує гру у відгадування слів."""
        socketserver.ThreadingTCPServer.__init__(self, server_address,
                                                    RequestHandlerClass)
        self.glist = Rlist()        # кільцевий список гравців (відгадувачів)
                                    # типу NetGuesser
        self.num_guessers = 0       # поточна кількість гравців
        self.num_to_start = NUM_TO_START  # кількість гравців для початку гри
        self.game_on = False        # чи йде гра
        self.word = ''              # слово для відгадування
        self.guessed = ''           # слово,заповнене '*'


class RequestHandler(socketserver.StreamRequestHandler):
    """Клас обробляє запити одного клієнта"""

    def handle(self):
        """Обробляє з'єднання одного гравця та підтримує його участь у грі."""
        print('connected from', self.client_address)
        self.name = None    # ім'я гравця
        done = self.server.game_on # done - чи завершено з'єднання
        if not done:
            name = self._readline()
            try:
                self.addGuesser(name)   # додати гравця
                # якщо гравці зібрались, то почати гру
                if self.server.num_guessers >= self.server.num_to_start:
                    self.startGame()
            except ClientError as error:
                print(error)
                self.privateMessage(error.args[0])
                done = True
            except socket.error as e:
                print(e)
                done = True

        # Вести гру
        while not done:
            try:
                done = self.processInput() # обробити отримані дані
            except ClientError as error:
                self.privateMessage(str(error))
            except socket.error as e:
                done = True

    def finish(self):
        """Автоматично викликається коли завершено метод handle()."""
        if self.name:
            # Гравець раніше успішно з'єднався.
            # Видалити його зі списку гравців 
            for i in range(self.server.glist.len()):
                netguesser = self.server.glist.getcurrent()
                if netguesser.getname() == self.name:
                    self.server.glist.delete()
                    self.server.num_guessers -= 1
                else:
                    self.server.glist.next()
        # якщо гравців не залишилось, поновити готовність до гри
        if self.server.glist.len() == 0:
            self.server.game_on = False
        print('disconnected', self.client_address)
        # завершити з'єднання
        self.request.shutdown(2)
        self.request.close()


    def processInput(self):
        """Читає рядок тексту та обробляє отриману команду."""
        done = False
        line = self._readline()
        # отримати команду та аргументи
        command, arg = self._parseCommand(line)
        if command:
            # викликати метод для виконання команди
            done = command(arg)
        else:
            raise ClientError('Неочікувані дані від клієнта {}'.format(self.name))
        return done

    def addGuesser(self, name):
        """Додає нового відгадувача з ім'ям name."""
        if not name:
            raise ClientError('Не надано імені гравця.')
        self.name = name
        # вставити гравця у список
        self.server.glist.insert(NetGuesser(self.name, self.wfile))
        self.server.num_guessers += 1
        # повідомити про приєднання гравця
        self.broadcast('До гри прєднався(лась) {}'.format(self.name))

    def startGame(self):
        """Починає гру."""
        self.server.game_on = True
        #ім'я файлу зі словами
        self.filename = os.pardir + '/' + os.pardir + '/' + \
                        'Lect_Python/T14/' + filename
        #вибрати слово з файлу для відгадування
        word, guessed = makeword(self.filename) 
#        print('word', word, 'guessed', guessed)
        self.server.word = word
        self.server.guessed = guessed
        # повідомити про початок гри та слово
        self.broadcast('Гра почалась!')
        self.broadcast('Слово: {}'.format(self.server.guessed))
        # надати хід першому гравцю
        self.nextTurn()

    def endGame(self):
        """Завершує гру."""
        # побудувати рядок результатів, розділений \n
        results = ''
        for i in range(self.server.glist.len()):
            netguesser = self.server.glist.getcurrent()
            self.server.glist.next()
            results = results + str(netguesser) + '\n'
        # повідомити про закінчення та показати результати
        self.broadcast('Гру закінчено!')
        self.broadcast(results)
        # надіслати клієнтам команду завершення роботи
        self.broadcast(QUIT)
        
    def nextTurn(self):
        """Надає гравцю хід."""
        netguesser = self.server.glist.getcurrent()
        # повідомляє всіх про те, у кого хід
        self.broadcast('Хід {}'.format(netguesser.getname()))
        # надсилає гравцю команду поточного ходу (TURN)
        netguesser.wfile.write(bytes(self._ensureNewline(TURN),
                                     encoding='utf-8'))
        
    # Реалізація команд сервера.
    
    def letterCommand(self, letter):
        """Команда /letter (літера)."""
        if letter in self.server.guessed: # літеру вже відгадано
            self.privateMessage('Літеру вже відгадано')
            self.nextTurn() # надіслати команду /turn
            done = False
        else:
            self.broadcast("Названо літеру '{}'".format(letter), False)
            points = 0
            gw = ""
            #замінюємо у guessed всі '*" у місцях входження letter до word на letter
            for i in range(len(self.server.word)):  
                if self.server.word[i] == letter:
                    gw = gw + letter    #дописуємо символ letter до слова відгадування
                    points += 1         #збільшуємо бали на 1
                else:
                    #дописуємо той символ який був у guessed
                    gw = gw + self.server.guessed[i]
            self.server.guessed = gw
            # повернути результат обробки балів (чи закінчено гру)
            done = self._processResults(points)
        return done

    def wordCommand(self, word):
        """Команда /word (слово)."""
        self.broadcast('Названо слово "{}"'.format(word), False)
        if word == self.server.word:  #слово відгадано
            #додаємо балів стільки, скільки було * 
            points = self.server.guessed.count('*') 
            self.server.guessed = self.server.word
        else:                       #слово не відгадано
            points = -1             #-1 означає, що треба очистити всі бали
        # повернути результат обробки балів (чи закінчено гру)
        return self._processResults(points)

    def _processResults(self, points):
        """Обробляє бали гравця points.

           Вирішує, чи завершено гру та чи треба передати хід.
           Повертає значення True/False: чи закінчено гру."""
        gameover = False    # чи завершено гру
        netguesser = self.server.glist.getcurrent() # потоний гравець
        if points > 0: # якщо бали зароблено
            netguesser.inc(points)
            self.privateMessage('Ви заробили балів: {}'.format(points))
            gameover = not '*' in self.server.guessed
            if gameover:
                self.privateMessage('Вітаємо! Ви виграли!!!')
                #премія за відгадування слова
                netguesser.inc(len(self.server.word))
        elif points < 0: # якщо не відгадано слово
            self.privateMessage('На жаль, Ваші бали "згоріли"')
            netguesser.clear()
        else:                       #points == 0, не відгадано літеру
            self.privateMessage('Немає такої літери')
        self.server.glist.update(netguesser)   #оновити дані гравця у списку
        # показати всім оновлене слово після відгадування
        self.broadcast('Слово: {}'.format(self.server.guessed))
        if gameover:
            self.endGame()  # завершити гру
        else:
            if points <= 0:
                # передати хід наступному гравцю
                self.server.glist.next()
            self.nextTurn() # надіслати команду /turn
        return gameover


    # Допоміжні методи.
    
    def broadcast(self, message, includeThisUser=True):
        """Розіслати повідомлення message всім клієнтам.

           Повідомлення відпправляється всім приєднаним клієнтам,
           окрім, можливо, поточного, що встановлюється параметром
           includeThisUser."""
        message = bytes(self._ensureNewline(message), encoding='utf-8')
        for i in range(self.server.glist.len()):
            netguesser = self.server.glist.getcurrent()
            self.server.glist.next()
            if includeThisUser or netguesser.getname() != self.name:
                netguesser.wfile.write(message)

    def privateMessage(self, message):
        """Надіслати повідомлення тільки поточному клієнту."""
        self.wfile.write(bytes(self._ensureNewline(message), encoding='utf-8'))

    def _readline(self):
        """Читає з мережі рядок, видаляє пропуски з початку та кінця."""
        line = str(self.rfile.readline().strip(), encoding='utf-8')
#        print(line)
        return line

    def _ensureNewline(self, s):
        """Запевняє, що рядок завершується символом '\n'."""
        if s and s[-1] != '\n':
            s += '\n'
        return s

    def _parseCommand(self, inp):
        """Намагається розібрати рядок як команду серверу.

           Якщо цю команду реалізовано, викликає відповідний метод.
        """
        commandMethod, arg = None, None
        # якщо рядок непорожній та починається з '/'
        if inp and inp[0] == '/':
            if len(inp) < 2:
                raise ClientError('Недопустима команда: "{}"'.format(inp))
            # список з 2 (або 1) значень: команда та її аргументи (якщо є)
            commandAndArg = inp[1:].split(' ', 1) 
            if len(commandAndArg) == 2: # є аргументи
                command, arg = commandAndArg
            else:
                command, = commandAndArg # немає аргументів
            # Чи реалізовано у класі метод, який починається
            # ім'ям команди та завершується 'Command'
            commandMethod = getattr(self, command + 'Command', None)
            if not commandMethod:
                raise ClientError('Немає такої команди: "{}"'.format(command))
        return commandMethod, arg


HOST = ''                 # Комп'ютер для з'єднання
PORT = 30003              # Порт для з'єднання

if __name__ == '__main__':
    print('=== WordGuess server ===')
    # запустити сервер
    WordGuessServer((HOST, PORT), RequestHandler).serve_forever()    
