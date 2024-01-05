#T14s3_12
#перевірка, чи є граф зв'язним

from T14.t14s3_11_graph import *

def fileinputgraph(filename, g):
    '''Вводить граф, записаний у текстовому файлі filename.

    Граф g повинен бути порожнім
    файл повинен мати вигляд:
    #коментар
    key1 0 [] []
    ...
    keyn 0 [] []
    key1 data1 [pred11,...,pred1m1] [succ11,...,succ1k1]
    ...
    keyn datan [predn1,...,prednmn] [succn1,...,succnkn]
    наприклад,
    #граф з 3 вершинами
    a 0 [] []
    b 0 [] []
    c 0 [] []
    a 2 [c] [b,c]
    b 5 [a] [c]
    c 23 [a,b] [a]
    '''
    f = open(filename)                  #відкрити файл filename
    for line in f:                      
        if len(line) > 0 and line[0] != '#': #якщо рядок не порожній та не коментар 
            parts = line.split()        #розбити рядок на список частин [ключ, дані, список попередників, список наступників]
            key = parts[0]              #key - ключ вершини - рядок
            data = parts[1]             #вважаємо що данні вершини data є рядком
            sp = parts[2][1:-1]         #sp - рядок зі списком попередників без дужок []
            ss = parts[3][1:-1]         #ss - рядок зі списком наступників без дужок []
            if len(sp) == 0:            #lp - список попередників
                lp = []
            else:
                lp = sp.split(',')
            if len(ss) == 0:            #ls - список наступників 
                ls = []
            else:
                ls = ss.split(',')
            t = (data, lp, ls)          #t - кортеж (дані, список попередників, список наступників)
            print(key, t)
            g[key] = t                  #встановити значення вершини графу key
    f.close()

def reachable(g, key, r):
    '''Будує множину вершин g, досяжних з вершини key.

    r - вже побудована множина досяжних вершин.
    '''
    ls = g.getsucceders(key)
    for k in ls:
        if not k in r:
            r.add(k)                    #додати вершину k до r
            rk = reachable(g, k, r)     #отримати множину вершин rk, досяжних з вершини k
            r = r | rk                  #об'єднати цю множину з r
    return r

def reducelist(slist):
    '''Зводить список множин досяжнх вершин slist.

    Якщо перетин 2 множин не порожній, - об'єднуємо їх.
    Об'єднання додаємо в кінець нового списку.
    '''
    wasunited = True                    #wasunited - чи було хоча б одне об'єднання множин
    while len(slist) > 1 and wasunited:
        wasunited = False
        n = len(slist)
        i = 0
        while i < n:                    #один прохід по списку
            i = i+1
            newlist = []                #newlist - новий список множин
            r = slist[0]
            for j in range(1, len(slist)):
                rj = slist[j]
                if len(r & rj) > 0:     #якщо є перетин r та rj, об'єднуємо їх
                    r = r | rj
                    n = n-1             #фіксуємо зменшення довжини списку множин на 1
                    wasunited = True
                else:
                    newlist.append(rj)  #якщо немає об'єднання, додаємо rj до нового списку
            newlist.append(r)           #додаємо r до кінця нового списку (повторно його розглядати не будемо) 
            slist = newlist
    return slist

def isconn(g):
    '''Перевіряє, чи є граф g зв'язним.

    '''
    nd = g.nodes()
    print('\n',nd)
    slist = []                              #slist - список множин досяжних вершин
    for k in nd:
        slist.append(reachable(g, k, {k}))  #будуємо список множин досяжних вершин
                                            #для кожної вершини
    print('до reducelist',slist)
    slist = reducelist(slist)               #зводимо цей список до 1 елемента або
                                            #розбиття на множини, що не перетинаються
    print('після reducelist',slist)
    return len(slist) <= 1

if __name__ == '__main__':
    filename = input("Введіть ім'я файлу: ")
    g = Graph()
    fileinputgraph(filename, g)
    if isconn(g):
        print("Граф є зв'язним")
    else:
        print("Граф не є зв'язним")

