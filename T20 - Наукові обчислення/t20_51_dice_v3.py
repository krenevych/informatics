#T20_51_v3
#Кидання костей. Ймовірність одночасного випадання шісток
#Метод Монте-Карло
#Векторизована версія
#Зображення гістограм


import numpy as np
import matplotlib.pyplot as plt

TEST_NUM = 10000

def draw_histogram(dices, sums, ndice, nroll):
    '''Зображує гістограму розподілу сум ndice костей та гістограму
       кількості ndice шісток у nroll киданнях.

       dices - результати випробувань, TEST_NUM раз по ndice костей.
       sums - кількість одночасно по ndice шісток у nroll киданнях для
              TEST_NUM випробувань.
    '''
    n_dices = np.sum(dices, axis = 1)

    bns = 6*ndice - ndice + 1                   #кількість варіантів сум
                                                #з ndice костей
    plt.subplot(1, 2, 1)                        #перший підграфік
    plt.hist(n_dices, bins=bns, color='r')      #зображення гістограми          
    plt.xlabel("Sum of {} dices".format(ndice)) #мітка осі x
    plt.ylabel("Frequency")                     #мітка осі y

    plt.subplot(1, 2, 2)                            #другий підграфік
    plt.hist(sums, bins = np.max(sums), color='g')  #зображення гістограми
    plt.xlabel("Quantity of {} '6'".format(ndice))  #мітка осі x
    plt.ylabel("Frequency")                         #мітка осі x
    plt.title("Histogram for {} rolls".format(nroll))#заголовок підграфіку

    plt.show()
    

def ndice_six_prob(ndice, nroll, show_hist = False):
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

    if show_hist:
        draw_histogram(dices, sums, ndice, nroll)

    success = len(sums[sums > 0])   #довжина масиву з додатних елементів sums
    return success / TEST_NUM


ndice = int(input('Кількість костей: '))
nroll = int(input('максимальна кількість кидань: '))

for rolls in range(1,nroll+1):
#rolls = nroll
    print('Ймовірність випадання {} 6 у {} киданнях = {}'.format(ndice,
                    rolls, ndice_six_prob(ndice, rolls, rolls == nroll)))

