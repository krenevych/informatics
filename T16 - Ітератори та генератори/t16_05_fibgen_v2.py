#T16_05_v2
#Генерація чисел Фібоначчі з зупинкою

def fibgen(n):
    '''Генератор-функція чисел Фібоначчі до n.'''
    i = 0
    a, b = 1, 1
    while True:
        i = i + 1
        if i > n:                   #якщо дійшли до n              
            raise StopIteration     #зупиняємось
        yield b
        a, b = b, a + b

n = int(input('n=? '))

print('Числа Фібоначчі')
i=0
for x in fibgen(n):
    i = i + 1
    print(i, x)


    
