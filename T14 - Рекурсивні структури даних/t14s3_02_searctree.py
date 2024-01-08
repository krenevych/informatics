#T14s3_02
#Побудова та пошук у дереві пошуку

from T14.t14s3_01_btree import *
import random


sconst = "зв'язування між об'єктами та методами поняття віртуальних методів поліморфізм"

def makewords(s = sconst):
    '''Будує список слів.

    '''
    words = s.split()
    random.shuffle(words) #перемішує слова у списку
    return words

def _searchplace(w, t1, t2):
    '''Шукає місце для w у дереві t1, використовуючи допоміжне дерево t2.

    Якщо w знайдено у дереві t1, то found == True.
    Якщо w не знайдено, то t1 - порожнє дерево, а t2 - батько t1.
    '''
    found = False
    if not t1.isempty():
        if t1.root() == w: #якщо корінь дорівнює w, то знайшли
            found = True
        elif t1.root() > w:#якщо корінь більше w, то йдемо ліворуч
            t1, t2 = t1.leftson(), t1
            found, t1, t2 = _searchplace(w, t1, t2)
        else:              #якщо корінь менше w, то йдемо праворуч
            t1, t2 = t1.rightson(), t1
            found, t1, t2 = _searchplace(w, t1, t2)
    return found, t1, t2
            
def buildtree(seq):
    '''Будує дерево пошуку t за послідовністю seq.

    '''
    t = Btree()
    if len(seq) > 0:
        t.updateroot(seq[0])    #щоб не розбиратись окремо з першим вузлом дерева
    for w in seq:
        found, t1, t2 = _searchplace(w, t, Btree())
        if not found:
            son = Btree()
            son.updateroot(w)   #утворюємо дерево з 1 вузлом
            if t2.root() > w:
                t2.updateleft(son) #приєднуємо як лівого сина
            else:
                t2.updateright(son)#приєднуємо як правого сина 
    return t
                
def searchtree(w, t):
    '''Шукає w у дереві t.

    '''
    found, t1, t2 = _searchplace(w, t, Btree())
    return found

if __name__ == '__main__':        
    words = makewords()
    t = buildtree(words)
    print(words)
    print('\nВведіть слова. "" - завершення')
    while True:
        w = input('?')          #вводимо слова для пошуку у дереві
        if len(w) == 0: break
        found = searchtree(w, t)
        print(found)


