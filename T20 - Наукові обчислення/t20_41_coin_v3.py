#T20_41_v3
#Кидання монети. Різниця кількості орлів та решок та ймовірність орлів
#Виведення графіків точками
#Логарифмічна шкала

import numpy as np
import matplotlib.pyplot as plt


n = int(input('Максимальна степінь: '))
flips = np.random.random_integers(0, 1, 2**n) #усі результати випробувань
r = np.arange(n+1)
x = 2**r                                        #масив точок 2**i
numheads = np.zeros(n+1, dtype = 'int64')       #кількість орлів
numtails = np.zeros(n+1, dtype = 'int64')       #кількість решок
diffs = np.zeros(n+1, dtype = 'int64')          #різниці між орлами та решками
probs = np.zeros(n+1)                           #ймовірність орлів
                                                #кількості решок

print("Крок Кількість      Орлів      Решок      Різниця    Ймовірність")    
for i, t in enumerate(x):
    numheads[i] = np.sum(flips[:t])
    numtails[i] = t - numheads[i]
    diffs[i] = abs(numheads[i]-numtails[i])
    probs[i] = numheads[i] / t
    print('{:4} {:10} {:10} {:10} {:10}    {:<25}'.format(i,
                t, numheads[i], numtails[i], diffs[i], probs[i]))

plt.subplot(2, 1, 1)                        #перший підграфік
plt.plot(x, diffs, 'ob', label = "Diff")    #створити графік з легендою
plt.legend()
plt.semilogx()                              #встановити логарифмічну шкалу x

plt.subplot(2, 1, 2)                        #другий підграфік
plt.plot(x, probs, 'or', label = "Prob")    #створити графік з легендою
plt.legend()
plt.semilogx()                              #встановити логарифмічну шкалу x
plt.show()

