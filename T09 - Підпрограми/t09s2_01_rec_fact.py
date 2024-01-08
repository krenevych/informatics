#T09s2_01
#Обчислення факторіалу з використанням рекурсії

def fact (n):
    if n == 0:
        y = 1
    else:
        y = n*fact(n-1)
    return y

n = int(input("введіть число: "))


print('{}!={}'.format(n,fact(n)))





