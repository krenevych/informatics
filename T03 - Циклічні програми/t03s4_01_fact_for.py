#T03s4_01
#Обчислення n! за допомогою циклу for

n = int(input('введіть n: '))
p = 1

for i in range(1, n + 1):
    p = p * i

print(n, '!=', p)
