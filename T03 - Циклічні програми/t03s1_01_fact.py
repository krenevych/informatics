#T03s1_01
#Обчислення n! за допомогою циклу while

n = int(input('введіть n: '))
p = 1
i = 0

while i < n:
    i = i + 1
    p = p * i
#    print('i =', i, 'p =', p)

print (n, '!=', p)
