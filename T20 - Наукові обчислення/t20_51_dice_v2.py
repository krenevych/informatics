#T20_51_v2
#Кидання костей. Ймовірність одночасного випадання шісток
#Метод Монте-Карло
#Векторизована версія


import numpy as np
#import matplotlib.pyplot as plt

TEST_NUM = 10000

def ndice_six_prob(ndice, nroll):
    '''Обчислює ймовірність одночасного випадання ndice шісток у nroll киданнях.

    '''
    #dices - масив випадкових результатів кидань окремих костей від 1 до 6
    dices = np.random.random_integers(1, 6, TEST_NUM * nroll * ndice)
#    print(dices)
    #Переформатовуємо цей масив у двовимірний. Другий вимір - кількість костей
    dices.shape = (TEST_NUM * nroll, ndice)
#    print(dices)
    #sixes - масив з ndice 6
    sixes = np.zeros(ndice, dtype = np.int) + 6
#    print(sixes)
    #equals - масив бульових величин, який для кожного рядка dices 
    #містить True, якщо у цьому рядку самі шістки, та False, якщо це не так
    equals = np.all(dices == sixes, axis = 1)
#    print(equals)
    #Переформатовуємо equals так, щоб він містив TEST_NUM рядків та nroll стовпчиків 
    equals.shape = (TEST_NUM, nroll)
    #sums містить суми рядків масиву equals. При цьому бульові величини
    #інтерпретуються як цілі (True - 1, False - 0)
    #отже sums містить кількість комбінацій з ndice шісток для кожного випробування
    #з nroll кидань
    sums = np.sum(equals, axis = 1)
#    print(sums)
    success = len(sums[sums > 0])   #довжина масиву з додатних елементів sums
    return success / TEST_NUM


ndice = int(input('Кількість костей: '))
nroll = int(input('максимальна кількість кидань: '))

for rolls in range(1,nroll+1):
#rolls = nroll
    print('Ймовірність випадання {} 6 у {} киданнях = {}'.format(ndice,
                    rolls, ndice_six_prob(ndice, rolls)))

