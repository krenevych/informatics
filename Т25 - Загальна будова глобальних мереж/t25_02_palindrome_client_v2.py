# t25_02_v2 Клієнт паліндром
# Відправляє на сервер рядок для перевірки, чи є він паліндромом
# Використовує файлоподібні об'єкти для обміну даними

import socket

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 20002          # Порт для з'єднання з сервером

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # з'єднатися з сервером
# створити об'єкти для обміну даними по аналогії з файлами
inp = s.makefile('rb', 0) # буферизацію відключено
out = s.makefile('wb', 0) # буферизацію відключено
while True:
    to_send = input('?: ') # ввести рядок для перевірки
    if not to_send: break
    # перетворити у рядок байтів та передати серверу
    out.write(bytes(to_send, encoding='utf-8') + b'\n')
    data = inp.readline()   # отримати відповідь сервера
    print('received')
    b = bool(data[:-1])     # перетворити до бульового типу
    if b:
        print(to_send, ' - pal')
    else:
        print(to_send, ' - not pal')

s.close()                   # завершити з'єднання

