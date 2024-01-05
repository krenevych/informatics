#T17_11_v3
#Декоратор для обчислення часу виконання функції

import functools

def benchmark(f):
    '''Декоратор @benchmark для обчислення часу виконання функції f.

    '''
    import time
    @functools.wraps(f)             #декоратор оновлює значення атрибутів
                                    #_benchmark відповідними атрибутами f
    def _benchmark(*args, **kw):
        t = time.clock()            #вимірюємо час перед викликом функції
        rez = f(*args, **kw)        #викликаємо f
        t = time.clock() - t        #вимірюємо різницю у часі після виклику функції
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark
        
