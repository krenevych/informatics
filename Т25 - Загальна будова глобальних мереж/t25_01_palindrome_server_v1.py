# t25_01_v1 Сервер паліндромів
# Очікує передачі рядка та перевіряє, чи є він паліндромом

import socket
import re


def test_palindrome(string):
    '''Перевіряє, чи є рядок string паліндромом.'''
    # видалити всі символи-розділювачі
    string = re.sub(r'''[ !?.,+:;"'()\-]+''', '', string)
    string = string.lower() # перевести до нижнього регістру
#    print(string)
    return string == string[::-1]


HOST = ''                 # Комп'ютер для з'єднання
PORT = 20002              # Порт для з'єднання

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))        # зв'язати з комп'ютером та портом
s.listen(1)                 # очікувати на з'єднання
conn, addr = s.accept()     # отримати параметри з'єднання
print('Connected by', addr)
while True:
    data = conn.recv(1024)  # отримати дані (рядок байтів)
    if not data: break      # якщо рядок порожній, закінчити
    # перетворити рядок байтів у рядок символів
    pal = str(data, encoding = 'utf-8')
#    print(pal)
    # перевірити на паліндром та відправити відповідь
    res = bytes(test_palindrome(pal)) + b'\n'
#    print(res)
    conn.sendall(res)
conn.close()                # закрити з'єднання
