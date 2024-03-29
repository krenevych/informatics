#T15_11
#У текстовому файлі f записано цілі числа
#Переписати всі парні числа у файл g.
#Обробка помилок у файлах.

filename = input("Ім'я файлу: ")
try:
    f = open(filename, 'r')
#відкриваємо файл для читання, тут може бути помилка, якщо файл не знайдено
    g = open(filename+'_rez', 'w')
#відкриваємо файл для запису, тут може бути помилка,
#наприклад, якщо немає прав на створення нового файлу
    for line in f:
        k = int(line)
#отримуємо ціле число з рядка, тут може бути помилка, якщо у рядку не ціле число
        if k % 2 == 0:
            g.write(str(k)+'\n')
#пишем у файл результату, тут також може бути помилка,
#наприклад, якщо немає прав на запис у файл
except FileNotFoundError as fn:
    print('Файл не знайдено', fn.filename)
except OSError as e:
    print('Невідома помилка OS')
    raise e
except ValueError:
    print('У файлі - не ціле число')
else:
    f.close()
    g.close()
                       
