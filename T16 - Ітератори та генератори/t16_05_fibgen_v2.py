#t16_05_fibgen_v2.py
#Генерація чисел Фібоначчі з зупинкою

def fibgen(n):
    '''Генератор-функція чисел Фібоначчі до n.'''
    i = 0
    a, b = 1, 1
    while True:
        i = i + 1
        if i > n:                   #якщо дійшли до n              
            break                   #зупиняємось
        yield b
        a, b = b, a + b

n = int(input('n=? '))

print('Числа Фібоначчі')
i=0
fg = fibgen(n)
for x in fg:
    i = i + 1
    print(i, x)


    
