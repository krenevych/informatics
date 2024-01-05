#T09s1_41
#Обчислити середнє значення та медіану даного вектора з n дійсних компонент.

def inputvec (n = 10):
    v=[]
    for i in range(n):
        x = float(input('v[{}]='.format(i+1)))
        v.append(x)
    return v    

def average (*param):
    '''Обчислює середнє значення змінної кількості аргументів.

    Якщо кількість аргументів = 0, то повертає 0.
    '''
    n = len(param)
    s = 0
    for par in param:
        s += par
    if n > 0:
        s /= n
    return s
    

n=int(input("\nКількість компонент: "))

v = inputvec(n)
av = average(*v)

v.sort()
i = len(v) // 2
if len(v) % 2 == 1:
    median = v[i]
else:
    median = average(v[i-1], v[i])

print ('Середнє', av)
print ('Медіана', median)

