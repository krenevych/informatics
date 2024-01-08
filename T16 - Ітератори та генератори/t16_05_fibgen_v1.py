#T16_05_v1
#Генерація чисел Фібоначчі

def fibgen():
    '''Генератор-функція чисел Фібоначчі.'''
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b

n = int(input('n=? '))
fg = fibgen()
print('Числа Фібоначчі (next)')
for i in range(n):
    print(i+1, next(fg))


print('Числа Фібоначчі (for ... in ...)')
i=0
for x in fibgen():
    i = i + 1
    if i > n: break
    print(i, x)


    
