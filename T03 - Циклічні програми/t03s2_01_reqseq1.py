#T03s2_01
#Обчислення заданого елемента послідовності для РС 1 порядку

x = float(input('введіть x: '))
n = int(input('введіть n: '))
y = 1
k = 0

while k < n:
    k = k + 1
    y = -y * x / k

print ('Результат', y)
