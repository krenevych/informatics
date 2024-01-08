#T03s3_01_v2
#Обчислення експоненти. Використання break

x = float(input('введіть x: '))
eps = float(input('введіть eps: '))
y = 1
z = 1
k = 0

while True:
    k = k + 1
    z = z * x / k
    if abs(z) < eps:
        break
    y = y + z


print ('Результат', y)
