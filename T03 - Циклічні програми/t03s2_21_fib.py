﻿#T03s2_01
#Обчислення заданого числа Фібоначчі (РС 2 порядку)

n = int(input('введіть n: '))
u = 1
v = 1
k = 1

while k < n + 1:
    k = k + 1
    t = u + v
    u = v
    v = t
    print('k =', k, 'f1 =', u, 'f2 =', v, 't =', t)

print ('Результат', u)
