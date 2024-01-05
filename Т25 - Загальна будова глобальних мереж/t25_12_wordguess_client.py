# t25_12 Клієнт гри у відгадування слів
# Отримує від сервера команди та рядки для показу
# Відправляє на сервер літери або слова
# Використовує файлоподібні об'єкти для обміну даними


import socket

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 30003          # Порт для з'єднання з сервером

class ServerError(Exception):
    "Виключення у разі отримання неправильних даних від сервера."
    pass


class WordGuessClient:
    """Клас клієнта гри у відгадування слів."""
    
    def __init__(self, host, port, name):
        """Встановити з'єднання з сервером."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        # створити файлоподібні об'єкти для обміну даними
        self.input = self.socket.makefile('rb', 0)
        self.output = self.socket.makefile('wb', 0)
        self.sendMessage(name)          # надіслати ім'я на сервер.
        self.run()                      # вести гру

    def run(self):
        """Веде гру, приймає та відправляє дані."""
        done = False
        # Вести гру
        while not done:
            try:
                done = self.processInput() # обробити отримані дані
            except ServerError as error:
                print(error)
                done = self.quitCommand()
            except socket.error as e:
                print(e)
                done = self.quitCommand()

    def sendMessage(self, message):
        """Відправити повідомлення серверу."""
        self.output.write(bytes(message + '\r\n', encoding='utf-8'))

    def processInput(self):
        """Читає рядок тексту від сервера та обробляє отриману команду.

           Якщо рядок не є командою, - показує його.
        """
        done = False
        line = self._readline()
        # отримати команду та аргументи
        command, arg = self._parseCommand(line)
        if command:
            # викликати метод для виконання команди
            # та передати параметри, якщо є
            if arg:  
                done = command(arg)
            else:
                done = command()
        else:   # якщо не команда, - просто показати рядок
            print(line) 
        return done

    def turnCommand(self):
        """Команда /turn (зробити хід)."""
        while True:
            m = input("1 - літера, 2 - слово: ")[0]
            if m == '1' or m == '2': break
        if m == '1':                            #літера
            c = input('літера: ')[0]
            message = '/letter {}'.format(c)
        else:                                   #слово
            w = input('слово: ')
            message = '/word {}'.format(w)
        self.sendMessage(message)   # відправити команду та дані серверу
        return False

    def quitCommand(self):
        """Команда /quit (завершити роботу)."""
        self.socket.shutdown(2)     # закрити "файли"
        self.socket.close()         # закрити з'єднання
        return True

    def _parseCommand(self, inp):
        """Намагається розібрати рядок як команду клієнту.

           Якщо цю команду реалізовано, викликає відповідний метод.
           Якщо рядок не є командою, - показує його.
        """
        commandMethod, arg = None, None
        # якщо рядок непорожній та починається з '/'
        if inp and inp[0] == '/':
            if len(inp) < 2:
                raise ServerError('Недопустима команда: "{}"'.format(inp))
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
                raise ServerError('Немає такої команди: "{}"'.format(command))
        return commandMethod, arg

    def _readline(self):
        """Читає з мережі рядок, видаляє пропуски з початку та кінця."""
        line = str(self.input.readline().strip(), encoding='utf-8')
#        print(line)
        return line


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:              # якщо не вистачає параметрів, ввести
        host = HOST
        port = PORT
        name = input("Введіть ім'я: ")
    else:
        host = sys.argv[1]     # 1 параметр
        port = sys.argv[2]     # 2 параметр
        name = sys.argv[3]     # 3 параметр

    wg = WordGuessClient(host, port, name)

