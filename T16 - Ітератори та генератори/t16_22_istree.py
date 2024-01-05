#T16_22
#перевірка, чи є граф деревом

from T16.t16_21_graphit import *
from T14.t14s3_12_congraph import *

def istree(g):
    '''Перевіряє, чи є граф g деревом.

    '''
    #отримати список напівстепенів входу всіх вершин 
    lst = [g.hdegin(k) for k in g] #for k in g використовує ітератор
    print(lst)
    return max(lst) <= 1 and lst.count(0) == 1 and isconn(g)
        
if __name__ == '__main__':
    filename = input("Введіть ім'я файлу: ")
    g = GraphIt()
    fileinputgraph(filename, g)
    if istree(g):
        print("Граф є деревом")
    else:
        print("Граф не є деревом")

