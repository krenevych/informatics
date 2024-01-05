#T03s4_11
#Обчислення n!! за допомогою циклу for

n = int(input('введіть n: '))
p = 1

for i in range(n,1,-2):
    p *= i

print (n,'!!=',p)
