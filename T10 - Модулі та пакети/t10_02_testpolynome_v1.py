#T10_02_v1
#Тестування модуля поліномів

import t10_01_polynome

print('Введіть 1 поліном')
m = input("режим введення: 'n' - коефіцієнти та степені 's' - рядок: ")[0]
if m == 'n':
    p1 = t10_01_polynome.inputpoly()
else:
    s = input('рядок: ')
    p1 = t10_01_polynome.strtopoly(s)

print('Введіть 2 поліном')
m = input("режим введення: 'n' - коефіцієнти та степені 's' - рядок: ")[0]
if m == 'n':
    p2 = t10_01_polynome.inputpoly()
else:
    s = input('рядок: ')
    p2 = t10_01_polynome.strtopoly(s)

while True:
    print("\nВкажіть дію над поліномами:")
    k = input("\t'v' - значення p1 у точці\n\t'+' - p1+p2\n\t'-' - p1-p2"\
          "\n\t'*' - p1*p2\n\t'd' - похідна p1\n\t'e' - вихід: ")[0]
    if k == 'v':
        x = float(input('x = '))
        v = t10_01_polynome.valuepoly(p1,x)
        print ('Значення:',v)
    elif k == '+':
        p =t10_01_polynome.sumpoly(p1,p2)
        print('Сума p1+p2')
        t10_01_polynome.printpoly(p)
    elif k == '-':
        p = t10_01_polynome.diffpoly(p1,p2)
        print('Різниця p1-p2')
        t10_01_polynome.printpoly(p)
    elif k == '*':
        p = t10_01_polynome.multpoly(p1,p2)
        print('Добуток p1*p2')
        t10_01_polynome.printpoly(p)
    elif k == 'd':
        n = int(input('n = '))
        p = t10_01_polynome.derivpoly(p1,n)
        print(n,'похідна р1')
        t10_01_polynome.printpoly(p)
    elif k == 'e': break
        

