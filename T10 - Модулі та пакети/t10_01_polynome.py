#T10_01
#Модуль реалізації поліномів
'''Даний модуль реалізує дії над поліномами.

Поліном представлений у вигляді словника. Степінь - ключ, коефіцієнт - значення.
Зберігаються тільки степені з ненульовими коефіцієнтами.

Функції:
inputpoly () -> dict - Введення поліному з клавіатури.
strtopoly (s) -> dict - Перетворення рядка у поліном.
    Рядок повинен мати вигляд (наприклад):
    3.7*x**3 + 0.3*x**1 + -1.2*x**0
printpoly (p) - Показати поліном у вигляді рядка.
    Рядок буде мати вигляд (наприклад):
    3.7*x**3 + 0.3*x**1 + -1.2*x**0
valuepoly(p, x) -> float - Значення поліному p у точці x.
sumpoly(p1, p2) -> dict - Сума поліномів p1 + p2.
diffpoly(p1, p2) -> dict - Різниця поліномів p1 - p2.
multpoly(p1, p2) -> dict - Добуток поліномів p1 * p2.
derivpoly(p [, n = 1]) -> dict - n-та похідна поліному p.
'''

def inputpoly ():
    '''Введення поліному.
    '''
    p = {}
    n = int(input('Кількість ненульових коефіцієнтів: '))
    for i in range(n):
        k = int(input('Степінь: '))
        c = float(input('Коефіцієнт: '))
        p[k] = c
    p = _delzeroes(p)
    return p

def strtopoly (s):
    '''Перетворення рядка у поліном.

    Рядок повинен мати вигляд (наприклад):

    3.7*x**3 + 0.3*x**1 + -1.2*x**0

    Пробіли між коефіцієнтами та степенями не допускаються.
    Від'ємні коефіцієнти записувати як у прикладі вище.
    '''
    p = {}
    s = s.replace('+',' ')
    ls = s.split()  #розбиваємо на список одночленів
    for m in ls:
        c = m.split('*x**') #виділяємо степінь та коефіцієнт
        k = int(c[1])
        v = float(c[0]) 
        p[k] = v
    p = _delzeroes(p)
    return p

def printpoly (p):
    '''Показати поліном у вигляді рядка.

    Рядок буде мати вигляд (наприклад):
    3.7*x**3 + 0.3*x**1 + -1.2*x**0
    '''
    ls = [str(p[k])+'*x**'+str(k) for k in p]
    s = ' + '.join(ls)
    print(s)    

def valuepoly(p, x):
    '''Значення поліному p у точці x.
    '''
    return sum([p[k]*x**k for k in p])

def sumpoly(p1, p2):
    '''Сума поліномів p1 + p2.
    '''
    p = p1.copy()   #копіюємо p1, щоб його зміни не вплинули на фактичний параметр
    p.update(p2)    #утворюємо словник, що містить всі ключі p1 та p2
    p = {k:p1.get(k,0) + p2.get(k,0) for k in p} #p == p1 + p2
    return _delzeroes(p)

def diffpoly(p1, p2):
    '''Різниця поліномів p1 - p2.
    '''
    p = p1.copy()   #копіюємо p1, щоб його зміни не вплинули на фактичний параметр
    p.update(p2)    #утворюємо словник, що містить всі ключі p1 та p2
    p = {k:p1.get(k,0) - p2.get(k,0) for k in p} #p == p1 - p2
    return _delzeroes(p)

def multpoly(p1, p2):
    '''Добуток поліномів p1 * p2.
    '''
    p = {}     
    for k1 in p1:
        for k2 in p2:
            p[k1+k2] = p.get(k1+k2,0) + p1[k1]*p2[k2]
    return _delzeroes(p)

def derivpoly(p, n = 1):
    '''n-та похідна поліному p.

    Якщо n не вказано, то перша похідна
    '''
    pp = p.copy() #копіюємо p, щоб його зміни не вплинули на фактичний параметр
    for i in range(n):
        pp = {k-1:pp[k]*k for k in pp if k != 0} #обчислюємо похідну
    return _delzeroes(pp)
    
def _delzeroes(p):
    '''Повертає копію p без нульових елементів.

    Якщо всі нулі, то повертає поліном 0*x**0.
    '''
    pp = {k:p[k] for k in p if p[k] != 0}
    if len(pp) == 0:    #якщо всі нулі
        pp[0] = 0
    return pp

if __name__ == '__main__':
    p1 = strtopoly('3.7*x**3 + 0.3*x**1 + -1.2*x**0')
    print('р1')
    printpoly(p1)
    p2 = strtopoly('2.2*x**3 + -1.3*x**2 + 0.2*x**1')
    print('р2')
    printpoly(p2)
    v = valuepoly(p1,2)
    print('Значення p1 у точці x=2:',v)
    p = sumpoly(p1,p2)
    print('Сума p1+p2')
    printpoly(p)
    p = diffpoly(p1,p2)
    print('Різниця p1-p2')
    printpoly(p)
    p = multpoly(p1,p2)
    print('Добуток p1*p2')
    printpoly(p)
    p = derivpoly(p1,2)
    print('2 похідна р1')
    printpoly(p)



      


