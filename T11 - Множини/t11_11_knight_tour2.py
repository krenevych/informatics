#T11_11
#Тур коня2
#Знайти найкоротшу послідовність кроків коня на шаховій дошці
#для переходу з заданого поля на інше задане поле

cols = list('abcdefgh')     #стовпчики дошки
lines = list(range(1,9))    #рядки дошки

#множина доступних позицій дошки
#спочатку - вся дошка
chessboard = {(c,l) for c in cols for l in lines}

#Список можливих кроків коня
tries = [(i,j) for i in range(-2,3) for j in range (-2,3)\
         if i !=0 and j != 0 and abs(i) != abs(j)]

def nextstep (pos, i, j):
    '''Виконує наступний крок коня від позиції pos.

    Крок виконується на задану кількість по горизонталі (i) та вертикалі (j).
    Наприклад, якщо поточна позиція pos == ('c',3), i == 2, j == 1,
    то нова позиція - ('e',4)
    '''
    c = chr(ord(pos[0])+i)
    l = pos[1]+j
    return c, l

def isvalid (pos):
    '''Перевіряє, чи знаходиться позиція pos на дошці.

    Перевірка виконується для всіх позицій, які на даний момент ще не відвідані
    '''
    global chessboard
    return pos in chessboard
  

def knighttour (s1, endpos, tour):
    '''Виконує тур коня до кінцевої позиції endpos.

    tour - шлях коня, список позицій в оберненому порядку
    від кінцевої endpos до поточної
    s1 - множина граничних позицій
    s11 - нова множина граничних позицій
    '''
    global chessboard, tries
    ok = False
    if endpos in s1:
        ok = True
        tour.append(endpos) #початок побудови шляху
    else:
        s11= set()
        for p in s1:            #для всіх позицій з множини s1 з усіх можливих кроків 
            for (i,j) in tries: #будуємо нову граничну множину s11 
                (c,l) = nextstep(p,i,j)
                t = (c,l)
                if isvalid(t):
                    s11.add(t)
                    chessboard.remove(t)    #видаляємо t з подальшого розгляду
        ok = knighttour(s11, endpos, tour)
        if ok:
            for (i,j) in tries:
                (c,l) = nextstep(tour[0],i,j)
                t = (c,l)
                if t in s1:
                    tour.insert(0,t)    #шлях будується від кінцевої позиції
                    break
            else:
                print('Помилка: попередню позицію для {} не знайдено у множині {}'.format(tour[0],s1))
                exit(1)
    return ok
       

while True:
    p1 = input("введіть початкову клітинку: ")
    t = (p1[0],int(p1[1]))
    s1 = {t}
    if isvalid(t): break
    print("Клітинка повинна бути на дошці")

while True:
    p2 = input("введіть кінцеву клітинку: ")
    endpos = (p2[0],int(p2[1]))
    if isvalid(endpos): break
    print("Клітинка повинна бути на дошці")

tour = []        
ok = knighttour(s1, endpos, tour)

if ok:
    print('Шлях - ', tour)
else:
    print('Щось пішло не так...', tour,'\n', chessboard)





