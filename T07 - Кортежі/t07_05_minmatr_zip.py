#T07_05
#Обчислення мінімального елемента матриці з використанням функцій zip та map

m=int(input("кількість рядків: "))
n=int(input("кількість стовпчиків: "))
#введення матриці a
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        x = float(input('a[{},{}]='.format(i+1,j+1)))
        a[i].append(x)

#виведення матриці
print('\nМатриця')
for i in range(m):
    print(a[i])

min_el = a[0][0]    #присвоюємо мінімуму значення першого елемента першого рядка
for i in range(m):
    for j in range(n):
        if a[i][j] < min_el:    #якщо поточний елемент менше мінімуму
            min_el = a[i][j]    #виконуємо переприсвоєня
    

print('min=',min_el)


#обчислення мінімального елемента за допомогою спискоутворення та функції min
min_el2 = min([min(x) for x in a])
print('min2=',min_el2)

#обчислення мінімального елемента за допомогою функцій min, zip та map
min_el3 = min(map(min,zip(*a)))
print('min3=',min_el3)

#обчислення мінімального елемента за допомогою функцій min та map
min_el4 = min(map(min,a))
print('min4=',min_el4)

