#T15_01_v1
#Видалення елемента списку. Обробка помилок

n = int(input('Кількість елементів: '))

#введення списку
x = []
for i in range(n):
    try:
        k = int(input('Елемент ' + str(i+1) + ': '))
        x.append(k)
    except RuntimeError:
        print('RuntimeError')
    except ValueError:
        print('ValueError')
       
#видалення 1 елемента списку
while True:
    m = int(input('Елемент для видалення: '))
    try:
        x.remove(m)
    except ValueError:      #except буде виконано, якщо станеться помилка ValueError
        print ('Елемента немає у списку. Введіть інший')
    else:
        print(m, ' видалено')
        break

print('Список ', x)




m = int(input('Елемент для видалення: '))
x.remove(m)
print('Список ', x)
        
