#T09s1_01
#Обчислення НСК, функція обчислення НСД

def gcd (m, n):
    """ Обчислення Найбільшого спільного дільника
    """
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m

a = int(input("введіть 1 число: "))
b = int(input("введіть 2 число: "))

c = a*b//gcd(a,b)

print('НСК({},{})={}'.format(a,b,c))

help(gcd)




