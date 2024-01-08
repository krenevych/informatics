#T10_02_v2
#Тестування модуля поліномів

import t10_01_polynome as polynome

def inp_poly():
    print('\nВведіть поліном')
    m = input("режим введення: 'n' - коефіцієнти та степені 's' - рядок: ")[0]
    if m == 'n':
        p = polynome.inputpoly()
    else:
        s = input('рядок: ')
        p = polynome.strtopoly(s)
    return p

print('1 поліном')
p1 = inp_poly()
print('2 поліном')
p2 = inp_poly()

while True:
    print("\nВкажіть дію над поліномами:")
    k = input("\t'v' - значення p1 у точці\n\t'+' - p1+p2\n\t'-' - p1-p2"\
          "\n\t'*' - p1*p2\n\t'd' - похідна p1\n\t'e' - вихід: ")[0]
    if k == 'v':
        x = float(input('x = '))
        v = polynome.valuepoly(p1,x)
        print ('Значення:',v)
    elif k == '+':
        p = polynome.sumpoly(p1,p2)
        print('Сума p1+p2')
        polynome.printpoly(p)
    elif k == '-':
        p = polynome.diffpoly(p1,p2)
        print('Різниця p1-p2')
        polynome.printpoly(p)
    elif k == '*':
        p = polynome.multpoly(p1,p2)
        print('Добуток p1*p2')
        polynome.printpoly(p)
    elif k == 'd':
        n = int(input('n = '))
        p = polynome.derivpoly(p1,n)
        print(n,'похідна р1')
        polynome.printpoly(p)
    elif k == 'e': break
        

