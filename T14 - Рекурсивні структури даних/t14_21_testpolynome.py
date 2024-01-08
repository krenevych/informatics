#t14_21_testpolynome.py
#Тестування класу Polynome

from t14_20_polynome import Polynome

def inputpoly():
    """
    Функція для введення поліному з клавіатури
    як послідовносіті степенів та коефіцієнтів
    :return: об'єкт класу Polynome
    """
    p = Polynome()
    n = int(input('Кількість ненульових коефіцієнтів: '))
    for i in range(n):
        k = int(input('Степінь: '))
        c = float(input('Коефіцієнт: '))
        p.add_monom(k, c)
    return p


def inp_poly():
    """
    Функція для введення поліному з клавіатури
    як послідовносіті степенів та коефіцієнтів
    або з заданого рядка
    :return: об'єкт класу Polynome
    """
    print('\nВведіть поліном')
    m = input("режим введення: 'n' - коефіцієнти та степені 's' - рядок: ")[0]
    if m == 'n':
        p = inputpoly()
    else:
        s = input('рядок: ')
        p = Polynome.fromstring(s)
    return p


print('1 поліном')
p1 = inp_poly()
print('2 поліном')
p2 = inp_poly()
print('р1 =', p1, "степінь", p1.get_degree())
print('р2 =', p2, "степінь", p2.get_degree())


while True:
    print("\nВкажіть дію над поліномами:")
    k = input("\t'v' - значення p1 у точці\n\t'+' - p1+p2\n\t'-' - p1-p2"\
          "\n\t'*' - p1*p2\n\t'd' - похідна p1\n\t'e' - вихід: ")[0]
    if k == 'v':
        x = float(input('x = '))
        print ('Значення:', p1(x))
    elif k == '+':
        print('Сума p1+p2:', p1 + p2)
    elif k == '-':
        print('Різниця p1-p2:', p1 - p2)
    elif k == '*':
        print('Добуток p1*p2:', p1 * p2)
    elif k == 'd':
        n = int(input('n = '))
        print('{}-a похідна р1: {}'.format(n, p1.deriv(n)))
    elif k == 'e': break
