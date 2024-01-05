#T09s1_11
#Чи є рядок паліндромом

def issymmetry (s):
    '''Перевіряє рядок s на симетричність.

    '''
    return s == s[::-1]

def del_term (s, t):
    '''Видаляє з s усі символи-розділювачі, які є у рядку t.

    '''
    for c in t:
        s = s.replace(c,"")
    return s

def prepare_string (s):
    '''Готує рядок s до перевірки на симетричність.

    Видаляє з s усі символи-розділювачі та переводить рядок до нижнього регістру.
    '''
    r = del_term(s, " ,.!?:;-")
    return r.lower()

def ispalindrome (s):
    '''Перевіряє, чи є рядок s паліндромом.

    '''
    s = prepare_string(s)
    return issymmetry(s)



s = input("введіть рядок: ")

if ispalindrome(s):
    print('Рядок "{}" є паліндромом'.format(s))
else:
    print('Рядок "{}" не є паліндромом'.format(s))
    




