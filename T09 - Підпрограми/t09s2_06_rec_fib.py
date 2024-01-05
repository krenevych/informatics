#T09s2_06
#Обчислення чисел Фібоначчі з використанням рекурсії

def fib (n):
    if n <= 1:
        y = 1
    else:
        y = fib(n - 1) + fib(n - 2)
    return y

n = int(input("введіть число: "))


print('Fib({})={}'.format(n,fib(n)))





