#T09s2_21
#Тур коня.
#Знайти послідовність кроків коня на шаховій дошці
#для переходу з заданого поля на інше задане поле

cols = list('abcdefgh')
lines = list(range(1,9))

#Список можливих кроків коня
tries = [(i,j) for i in range(-2,3) for j in range (-2,3)\
         if i !=0 and j != 0 and abs(i) != abs(j)]
#Список відвіданих полів
visited = []

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

    '''
    global cols, lines
    return (pos[0] in cols) and (pos[1] in lines)
  

def knighttour (tour, endpos):
    '''Виконує тур коня до кінцевої позиції endpos.

    tour - шлях коня, список позицій від початкової до поточної
    '''
    global tries, visited
    ok = False              #ok залишиться False, якщо не кінець шляху та немає продовження
    if tour[-1] == endpos:  #якщо кінець шляху
        ok = True
    else:
        for (i,j) in tries: #перебираємо всі можливі ходи
            (c,l) = nextstep(tour[-1],i,j)
            t = (c,l)
            if isvalid(t) and not t in visited: #якщо поле на дошці та ще не відвідано
                tour.append(t)                  #додаємо його до шляху
                visited.append(t)               #та до списку відвіданих полів
                ok = knighttour(tour, endpos)   #шукаємо подальший шлях
                if ok:                          #якщо знайшли, то кінець
                    break
                else:
                    tour.pop()                  #інакше повертаємось на крок назад
    return ok
        
        
while True:
    s = input("введіть початкову клітинку: ")
    tour = [(s[0],int(s[1]))]
    visited = tour[:] #щоб все було правильно, visited треба присвоїти копію tour
    if isvalid(tour[0]): break
    print("Клітинка повинна бути на дошці")

while True:
    s = input("введіть кінцеву клітинку: ")
    endpos = (s[0],int(s[1]))
    if isvalid(endpos): break
    print("Клітинка повинна бути на дошці")

ok = knighttour(tour, endpos)

if ok:
    print('Шлях - ', tour)
else:
    print('Щось пішло не так...', tour,'\n', visited)





