#T06_11_v1
#Обчислення мінімального елемента матриці

m=int(input("кількість рядків: "))
n=int(input("кількість стовпчиків: "))
#введення матриці a
a=[]
for i in range(m):
    a.append([])
    for j in range(n):
        x = float(input('a[{},{}]='.format(i+1,j+1)))
        a[i].append(x)

min_el = a[0][0]                #присвоюємо мінімуму значення першого елемента першого рядка
for i in range(m):
    for j in range(n):
        if a[i][j] < min_el:    #якщо поточний елемент менше мінімуму
            min_el = a[i][j]    #виконуємо переприсвоєня
    

print('min=',min_el)



