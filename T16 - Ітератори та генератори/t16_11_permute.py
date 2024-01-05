#T16_11
#Отримання перестановок с n елементів
#Приклад взято з Learning Python. 5th Edition by Mark Lutz

def permute1(seq):
    '''Отримання всіх перестановок послідовності у вигляді списку.
    '''
    if not seq: 
        return [seq] #якщо послідовність порожня, повертаємо її
    else:
        result = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  #Видалити поточний елемент
            for x in permute1(rest):    #У всі перестановки інших елементів
                result.append(seq[i:i+1] + x) #Вставити поточний елемент у початок
    return result

def permute2(seq):
    '''Отримання всіх перестановок послідовності - генератор.
    '''
    if not seq:
        yield seq #якщо послідовність порожня, повертаємо її
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  #Видалити поточний елемент
            for x in permute2(rest):    #У всі перестановки інших елементів
                yield seq[i:i+1] + x    #Вставити поточний елемент у початок


def printall(func, seq):
    '''Друк усіх перестановок послідовності seq.

    Перестановки повертаються функцією func.
    '''
    d = func(seq)   #Повернути перестановки
    for x in d:
        print(x)

def printtop10(func, seq):
    '''Друк перших 10 перестановок послідовності seq.

    Перестановки повертаються функцією func.
    '''
    d = func(seq)   #Повернути перестановки
    d = iter(d)     #отримати ітератор з результатів функції func
    for i in range(10):
        print(next(d))
        
fs = [permute1, permute2]   #fs - список 2 функцій, що генерують перестановки
n = int(input('n=? '))
seq = list(range(n))
for f in fs:
    input('Натисніть Enter для продовження')
    print(f.__name__)
    if n < 7:
        printall(f, seq)
    else:
        printtop10(f, seq)
        
