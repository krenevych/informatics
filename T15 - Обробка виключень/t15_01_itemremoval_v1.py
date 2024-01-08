#T15_01_v1
#Видалення елемента списку. Обробка помилок

n = int(input('Кількість елементів: '))

#введення списку
x = []
for i in range(n):
    k = int(input('Елемент ' + str(i+1) + ': '))
    x.append(k)


#видалення 1 елемента списку
while True:
    try:
        m = int(input('Елемент для видалення: '))
        x.remove(m)
        print(m, ' видалено')
        break
    except ValueError:      #except буде виконано, якщо станеться помилка ValueError
        print ('Елемента немає у списку. Введіть інший')

print('Список ', x)
