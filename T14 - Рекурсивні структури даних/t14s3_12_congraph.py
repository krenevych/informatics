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

def isconn(g):
    '''Перевіряє, чи є граф g зв'язним.

    '''
    nd = list(g.nodes())                    # список вершин графа (ключів)
    nodes_reached = {nd[0]}                 # множина досягнутих вершин
    nodes_viewed = set()                    # множина вершин, що переглянуто
    while True:
        nodes_in_view = nodes_reached - nodes_viewed    # множина вершин,
                                                        # що досі не переглянуто
        if len(nodes_in_view) == 0: break
        for node in nodes_in_view:
            # додати до множини досягнутих вершин
            # усіх попередників та наступників вершини node
            nodes_reached = nodes_reached | set(g.getpredecessors(node)) \
                                        | set(g.getsucceders(node))
            nodes_viewed.add(node)              # додати node до множини
                                                # вершин, що переглянуто
    return len(nodes_reached) == len(g)     # чи множина досягнутих вершин включає
                                        # всі вершини графа

if __name__ == '__main__':
    filename = input("Введіть ім'я файлу: ")
    g = Graph()
    fileinputgraph(filename, g)
    if isconn(g):
        print("Граф є зв'язним")
    else:
        print("Граф не є зв'язним")

