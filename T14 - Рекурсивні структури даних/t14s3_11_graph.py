#T14s3_11
#Граф

class Graph:
    '''Реалізує орієнтований граф на базі словника.

    Кожна вершина графу має унікальний ідентифікатор key, а також трійку
    (data, predecessors, succeders),
    де
    data          дані вершини
    predecessors  список попередників
    succeders     список наступників
    '''
    def __init__(self):
        '''Створити порожній граф.
        '''
        self._dct = {}      #_dct - словник, що містить вершини графу

    def nodes(self):
        '''Вершини графу.
        '''
        return self._dct.keys()

    def __len__(self):
        '''Довжина графу, реалізує len(g).
        '''
        return len(self._dct)

    def __getitem__(self, key):
        '''Повернути вершину, реалізує g[key].

        Якщо вершини key немає у графі, повертає None.  
        '''
        if key in self._dct:
            value = self._dct[key]
        else:
            value = None
        return value

    def getdata(self, key):
        '''Повернути дані вершини.

        Якщо вершини key немає у графі, повертає None.  
        '''
        if key in self._dct:
            data = self._dct[key][0]
        else:
            data = None
        return data

    def getpredecessors(self, key):
        '''Повернути список попередників вершини.

        Якщо вершини key немає у графі, повертає None.  
        '''
        if key in self._dct:
            lst = self._dct[key][1]
        else:
            lst = None
        return lst

    def getsucceders(self, key):
        '''Повернути список наступників вершини.

        Якщо вершини key немає у графі, повертає None.  
        '''
        if key in self._dct:
            lst = self._dct[key][2]
        else:
            lst = None
        return lst

    def setdata(self, key, data):
        '''Оновити дані вершини key значенням data.

        Якщо вершини key немає у графі, видає помилку.  
        '''
        if key in self._dct:
            dt, lp, ls = self._dct[key]     #повертає дані, списки попередників та наступників
            self._dct[key] = (data, lp, ls) #встановлює нове значення вершини з даними data
        else:
            print('setdata: немає вершини', key)
            exit(1)

    def setpredecessors(self, key, lst):
        '''Оновити список попередників вершини key значенням lst.

        Якщо вершини key немає у графі, видає помилку.  
        '''
        if key in self._dct:
            dt, lp, ls = self._dct[key]     #повертає дані, списки попередників та наступників
            self._removeinpred(key)         #видаляє посилання на вершину key в усіх списках наступників старих попередників вершини
            self._dct[key] = (dt, lst, ls)  #встановлює нове значення вершини з новим списком попередників lst 
            self._addinpred(key)            #вставляє посилання на вершину key в усіх списках наступників нових попередників вершини
        else:
            print('setpredecessors: немає вершини', key)
            exit(1)

    def setsucceders(self, key, lst):
        '''Оновити список наступників вершини key значенням lst.

        Якщо вершини key немає у графі, видає помилку.  
        '''
        if key in self._dct:
            dt, lp, ls = self._dct[key]     #повертає дані, списки попередників та наступників
            self._removeinsucc(key)         #видаляє посилання на вершину key в усіх списках попередників старих наступників вершини 
            self._dct[key] = (dt, lp, lst)  #встановлює нове значення вершини з новим списком наступників lst
            self._addinsucc(key)            #вставляє посилання на вершину key в усіх списках попередників нових наступників вершини
        else:
            print('setsucceders: немає вершини', key)
            exit(1)

    def _removeinpred(self, key):
        '''Видалити вершину key із списків наступників усіх попередників вершини.
        '''
        if key in self._dct:
            p = self.getpredecessors(key)   #p - список попередників вершини key
#        if not p is None:
            for k in p:
                lst = self._dct[k][2]       #lst - список наступників вершини k
                lst.remove(key)

    def _removeinsucc(self, key):
        '''Видалити вершину key із списків попередників усіх наступників вершини.
        '''
        if key in self._dct:
            p = self.getsucceders(key)      #p - список наступників вершини key
#        if not p is None:
            for k in p:
                lst = self._dct[k][1]       #lst - список попередників вершини k 
                lst.remove(key)

    def _addinpred(self, key):
        '''Додати вершину key до списків наступників усіх попередників вершини.
        '''
        if key in self._dct:
            p = self.getpredecessors(key)   #p - список попередників вершини key     
#        if not p is None:
            for k in p:
                lst = self._dct[k][2]       #lst - список наступників вершини k
                lst.append(key)

    def _addinsucc(self, key):
        '''Додатии вершину key до списків попередників усіх наступників вершини.
        '''
        if key in self._dct:
            p = self.getsucceders(key)      #p - список наступників вершини key
#        if not p is None:
            for k in p:
                lst = self._dct[k][1]       #lst - список попередників вершини k
                lst.append(key)

    def __delitem__(self, key):
        '''Видалити вершину графа key (del x[key]).

        Якщо вершини key немає у графі, видає помилку.  
        '''
        if key in self._dct:
            self._removeinpred(key) #видаляє посилання на вершину key в усіх списках наступників попередників вершини 
            self._removeinsucc(key) #видаляє посилання на вершину key в усіх списках попередників наступників вершини
            del self._dct[key]      #видаляє вершину з словника
        else:
            print('__delitem__: немає вершини', key)
            exit(1)

    def _addnode(self, key, value):
        '''Додати вершину графа key.

        Якщо вершини key немає у графі, видає помилку.  
        '''
        if not key in self._dct:
            self._dct[key] = value  #додає вершину до словника
            self._addinpred(key)    #вставляє посилання на вершину key в усіх списках наступників попередників вершини
            self._addinsucc(key)    #вставляє посилання на вершину key в усіх списках попередників наступників вершини
        else:
            print('_addnode: вже є вершина', key)
            exit(1)

    def __setitem__(self, key, value):
        '''Оновити (додати) вершину x[key] = value.

        Якщо вершини key немає у графі, додає її.  
        '''
        if not isinstance(value,tuple) or len(value) != 3 \
           or not isinstance(value[1], list)or not isinstance(value[2], list): #перевірити, чи правильно передані параметри
            print('x[key] = value: value must be tuple of 3' \
                  ' with lists on second and third place')
            exit(1)
        if key in self._dct:        #якщо вершина key є у графі
            self.__delitem__(key)   #спочатку видалити її
        self._addnode(key, value)   #додати вершину до графу з новим значенням value

