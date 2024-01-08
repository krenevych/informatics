# t25_02_v1 Клієнт паліндром
# Відправляє на сервер рядок для перевірки, чи є він паліндромом

import socket

HOST = 'localhost'    # Комп'ютер для з'єднання з сервером
PORT = 20002          # Порт для з'єднання з сервером

# створити гніздо
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # з'єднатися з сервером
while True:
    to_send = input('?: ') # ввести рядок для перевірки
    if not to_send: break
    # перетворити у рядок байтів та передати серверу
    s.sendall(bytes(to_send, encoding='utf-8'))
#    print('sent')
    data = s.recv(1024)     # отримати відповідь сервера
#    print('received')
    b = bool(data[:-1])     # перетворити до бульового типу
    if b:
        print(to_send, ' - pal')
    else:
        print(to_send, ' - not pal')
s.close()                   # завершити з'єднання

