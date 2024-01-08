#T03s3_01_v3
#Обчислення експоненти, демонстрація else після while.

x = float(input('введіть x: '))
eps = float(input('введіть eps: '))
y = 1
z = 1
k = 0

while abs(z) >= eps:
    k = k + 1
    z = z * x / k
    if abs(z) < eps:
        break
    y = y + z
else:
    print('цикл не виконався жодного разу, бажано зменшити значення eps')

print('Результат', y)
