#T16_31_v2
#Генератори-функції для обходу бінарного дерева

from T14.t14s3_01_btree import *


def klp_gen(t):
    '''Генератор-функція, що повертає всі вузли t у порядку КЛП
    '''
    if not t.isempty():
        yield t.root()                  #повернути корінь дерева           
        yield from klp_gen(t.leftson()) #рекурсивний виклик генератора для лівого сина
        yield from klp_gen(t.rightson())#рекурсивний виклик генератора для правого сина
        
def lkp_gen(t):
    '''Генератор-функція, що повертає всі піддерева t у порядку ЛКП
    '''
    if not t.isempty():
        yield from lkp_gen(t.leftson()) #рекурсивний виклик генератора для лівого сина
        yield t.root()                  #повернути корінь дерева 
        yield from lkp_gen(t.rightson())#рекурсивний виклик генератора для правого сина

def lpk_gen(t):
    '''Генератор-функція, що повертає всі піддерева t у порядку ЛПК
    '''
    if not t.isempty():
        yield from lpk_gen(t.leftson()) #рекурсивний виклик генератора для лівого сина
        yield from lpk_gen(t.rightson())#рекурсивний виклик генератора для правого сина
        yield t.root()                  #повернути корінь дерева


if __name__ == '__main__':
    from T14.t14s3_02_searctree import *

    #отримати список слів та перемішати його
    words = makewords()
    #побудувати бінарне дерево пошуку для цього списку слів
    t = buildtree(words)
    print(words)

    #отримуємо список усіх вузлів дерева у порядку обходу КЛП
    klp = [x for x in klp_gen(t)]
    print('\nКЛП\n', klp)

    #отримуємо список усіх вузлів дерева у порядку обходу ЛКП
    lkp = [x for x in lkp_gen(t)]
    print('\nЛКП\n', lkp)

    #отримуємо список усіх вузлів дерева у порядку обходу ЛПК
    lpk = [x for x in lpk_gen(t)]
    print('\nЛПК\n', lpk)

                           
    
