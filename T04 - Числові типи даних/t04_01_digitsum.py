#T04_01
#Обчислення суми цифр заданого невід'ємного цілого числа та показ всіх його цифр

while True:
    n = int(input('введіть n>=0: '))
    if n >= 0: break

s=0
print ('Цифри')
while True:
    a = n % 10
    print (a)
    s += a
    n //= 10
    if n == 0: break

print('Сума цифр',s)

