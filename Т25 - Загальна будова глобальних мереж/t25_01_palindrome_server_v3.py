# t25_01_v3 Сервер паліндромів
# Очікує передачі рядка та перевіряє, чи є він паліндромом
# Використовує TCPServer

import socketserver
import re


class RequestHandler(socketserver.StreamRequestHandler):
    """Обробляє запити одного клієнта"""

    def handle(self):
        """Обробляє з'єднання з клієнтами."""
        print('connected from', self.client_address)
        while True:
            # отримати дані
            data = self.rfile.readline().strip()
#            print(data)
            if not data: break
            pal = str(data, encoding = 'utf-8')
            # перевірити на паліндром та відправити відповідь
            res = bytes(self._test_palindrome(pal)) + b'\n'
#            print(res)
            self.wfile.write(res)
        print('disconnected', self.client_address)



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
    print('=== Palindrome server ===')
    socketserver.TCPServer((HOST, PORT), RequestHandler).serve_forever()    
