#T17_21
#Декоратор для трасування функції

import functools

def trace(debug = True):
    '''Декоратор @trace для відсліковування виконання функції f.

    Параметр debug вказує, чи здійснювати трасування
    '''
    def _trace(f):
        @functools.wraps(f)         #декоратор оновлює значення атрибутів
                                    #__trace відповідними атрибутами f
        def __trace(*args, **kw):
            if debug:
                print('вхід до',f.__name__) 
            rez = f(*args, **kw)    #викликаємо f
            if debug:
                print('вихід з',f.__name__)
            return rez
        return __trace
    return _trace
        
