#T09s2_01
#Обчислення факторіалу з використанням рекурсії

def fact (n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
 
n = int(input("введіть число: "))


print('{}!={}'.format(n,fact(n)))





