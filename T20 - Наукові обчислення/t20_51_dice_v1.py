#T20_51_v1
#Кидання костей. Ймовірність одночасного випадання шісток.
#Метод Монте-Карло


#import numpy as np
#import matplotlib.pyplot as plt
import random

TEST_NUM = 10000

def ndice_six_prob(ndice, nroll):
    '''Обчислює ймовірність одночасного випадання ndice шісток у nroll киданнях.

    '''
    #dices - тривимірний масив випадкових результатів кидань костей від 1 до 6
    #Перший вимір - кількість випробувань TEST_NUM
    #Другий вимір - кількість кидань nroll
    #Третій вимір - кількість костей ndice
    dices =[ [ [random.randint(1, 6) for k in range(ndice)]
               for j in range(nroll)] for i in range(TEST_NUM)]
#    print(dices)
    #sixes - масив з ndice 6
    sixes = [6] * ndice
    #sixcount - масив кількостей комбінацій з ndice самих шісток
    #для кожного окремого випробування з nroll кидань
    sixcount = [ rolls.count(sixes) for rolls in dices]
#    print(sixcount)
    #фільтруємо ті елементи sixcount, в яких
    #кількість комбінацій з ndice самих шісток більше 0
    #success - число таких елементів
    success = len(list(filter(lambda cnt: cnt > 0, sixcount)))
#    print(success)
    return success / TEST_NUM


ndice = int(input('Кількість костей: '))
nroll = int(input('максимальна кількість кидань: '))

for rolls in range(1,nroll+1):
    print('Ймовірність випадання {} 6 у {} киданнях = {}'.format(ndice,
                    rolls, ndice_six_prob(ndice, rolls)))

