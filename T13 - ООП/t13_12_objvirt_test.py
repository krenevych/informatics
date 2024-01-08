#T13_12_v2
#Тестування зв'язування об'єктів та методів, віртуальні методи

import turtle, random, t13_11_objvirt_v2

pause = 20
n = int(input('Циклів моделювання: '))

turtle.home()
turtle.delay(pause)

sh = []                         #список фігур на екрані
while n > 0:
    n -= 1
    m = random.randrange(1, 6)  #отримати режим роботи
    if m == 1: #додати точку
        x = random.randrange(-200,201)
        y = random.randrange(-200,201)
        p = t13_11_objvirt_v2.Point(x, y)
        sh.append(p)
        print('Додано точку ({},{}), номер фігури {}'.format(x,y,len(sh)-1))
    elif m == 2: #додати коло
        x = random.randrange(-200,201)
        y = random.randrange(-200,201)
        r = random.randrange(1,100)
        c = t13_11_objvirt_v2.Circle(x, y, r)
        sh.append(c)
        print('Додано коло з центром ({},{}), радіус {}, номер фігури {}'.format(x,y,r,len(sh)-1))
    elif m == 3: #зробити точку або коло видимим
        if len(sh) > 0:
            k = random.randrange(len(sh))
            sh[k].switchon()
            print('Фігура {} є видимою'.format(k))
    elif m == 4: #зробити точку або коло невидимим
        if len(sh) > 0:
            k = random.randrange(len(sh))
            sh[k].switchoff()
            print('Фігура {} не є видимою'.format(k))
    elif m == 5: #пермістити точку або коло
        if len(sh) > 0:
            k = random.randrange(len(sh))
            dx = random.randrange(-50,51)
            dy = random.randrange(-50,51)
            sh[k].move(dx, dy)
            print('Фігуру {} переміщено на {}, {}'.format(k, dx, dy))

turtle.bye()

t13_11_objvirt_v2.Point.printcount()
t13_11_objvirt_v2.Circle.printcount()


