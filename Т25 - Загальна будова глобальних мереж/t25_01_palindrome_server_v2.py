# t25_01_v2 Сервер паліндромів
# Очікує передачі рядка та перевіряє, чи є він паліндромом
# Використовує режим передачі файлу

import socket
import re

class PalindromeServer:

    def __init__(self, host_port):
        # створити гніздо
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # допустити повторне використання адреси та порту
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(host_port)        # зв'язати з комп'ютером та портом
        self.socket.listen(5)              # очікувати на з'єднання до 5 клієнтів одночасно
        print('=== Palindrome server ===')
    

    def run(self):
        """Обробляє з'єднання з клієнтами."""
        while True:
            print('** waiting for connection **')
            # очікувати на з'єднання клієнта
            conn, address = self.socket.accept()
            # перетворити вхід та вихід з'єднання на файли
            print(address)
            # створити об'єкти для обміну даними по аналогії з файлами
            input = conn.makefile('rb', 0) # буферизацію відключено
            output = conn.makefile('wb', 0) # буферизацію відключено
            try:
                while True:
                    data = input.readline().strip()
#                    print(data)
                    if data:
                        pal = str(data, encoding = 'utf-8')
                         # перевірити на паліндром та відправити відповідь
                        res = bytes(self._test_palindrome(pal)) + b'\n'
#                        print(res)
                        output.write(res)
                    else:
                        # Якщо рядок порожній, закрити з'єднання
                        conn.shutdown(2) # Закрити вхід та вихід.
            except socket.error as e:
                # Скоріше за все, клієнт роз'єднався.
                print(e)


    def _test_palindrome(self, string):
        '''Перевіряє, чи є рядок string паліндромом.'''
        # видалити всі символи-розділювачі
        string = re.sub(r'''[ !?.,+:;"'()\-]+''', '', string)
        string = string.lower() # перевести до нижнього регістру
    #    print(string)
        return string == string[::-1]


HOST = ''                 # Комп'ютер для з'єднання
PORT = 20002              # Порт для з'єднання

if __name__ == '__main__':
    ps = PalindromeServer((HOST, PORT))
    ps.run()
    
