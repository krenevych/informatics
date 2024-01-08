#T03s1_01_v0
#Обчислення n! за допомогою циклу while

n = int(input('введіть n: '))
p = 1

while n > 0:
    p = p * n
    n = n - 1

print('p=', p)
