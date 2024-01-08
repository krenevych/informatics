#T16_31_v1
#Класи-ітератори для обходу бінарного дерева

from T14.t14s3_01_btree import *
import T14.t14s1_01_stack as stack

class KLP:
    """Ітератор для реалізації обходу КЛП.

    """
    def _populate(self, t):
        """Наповнити стек піддеревами дерева t у порядку КЛП.
        """
        if not t.isempty():
            self._populate(t.rightson())    #спочатку правий син
            self._populate(t.leftson())     #потім лівий син
            self._st.push(t)                #потім корінь

    def __init__(self, t):
        self._st = stack.Stack()    #_st - стек, що містить піддерева дерева t
        self._populate(t)

    def __iter__(self):
        return self

    def __next__(self):
        if self._st.isempty():      #якщо стек порожній
            raise StopIteration     #зупиняємось
        else:
            t = self._st.pop()      #інакше повертаємо піддерево з верхівки стеку
            return t

class LKP(KLP):
    """Ітератор для реалізації обходу ЛКП.

    """
    def _populate(self, t):
        """Наповнити стек піддеревами дерева t у порядку ЛКП.
        """
        if not t.isempty():
            self._populate(t.rightson())    #спочатку правий син
            self._st.push(t)                #потім корінь
            self._populate(t.leftson())     #потім лівий син

class LPK(KLP):
    """Ітератор для реалізації обходу ЛПК.

    """
    def _populate(self, t):
        """Наповнити стек піддеревами дерева t у порядку ЛПК.
        """
        if not t.isempty():
            self._st.push(t)                #спочатку корінь
            self._populate(t.rightson())    #потім правий син
            self._populate(t.leftson())     #потім лівий син



if __name__ == '__main__':
    from T14.t14s3_02_searctree import *

    #отримати список слів та перемішати його
    words = makewords()
    #побудувати бінарне дерево пошуку для цього списку слів
    t = buildtree(words)
    print(words)

    #отримуємо список усіх вузлів дерева у порядку обходу КЛП
    klp = [x.root() for x in KLP(t)]
    print('\nКЛП\n', klp)

    #отримуємо список усіх вузлів дерева у порядку обходу ЛКП
    lkp = [x.root() for x in LKP(t)]
    print('\nЛКП\n', lkp)

    #отримуємо список усіх вузлів дерева у порядку обходу ЛПК
    lpk = [x.root() for x in LPK(t)]
    print('\nЛПК\n', lpk)

    
