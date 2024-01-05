# t27_01 Локальний веб-сервер

from http.server import HTTPServer, CGIHTTPRequestHandler

HOST = ''               # Комп'ютер для з'єднання
PORT = 8000             # Порт для з'єднання


print('=== Local webserver ===')
HTTPServer((HOST, PORT), CGIHTTPRequestHandler).serve_forever()    
