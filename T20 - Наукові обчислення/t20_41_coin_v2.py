#T20_41_v2
#Кидання монети. Різниця та відношення кількості орлів до решок
#Виведення графіків точками

import numpy as np
import matplotlib.pyplot as plt


n = int(input('Максимальна степінь: '))
flips = np.random.random_integers(0, 1, 2**n) #усі результати випробувань
r = np.arange(n+1)
x = 2**r                                        #масив точок 2**i
numheads = np.zeros(n+1, dtype = 'int64')       #кількість орлів
numtails = np.zeros(n+1, dtype = 'int64')       #кількість решок
diffs = np.zeros(n+1, dtype = 'int64')          #різниці між орлами та решками
ratios = np.zeros(n+1)                          #відношення кількості орлів до
                                                #кількості решок

print("Крок Кількість      Орлів      Решок      Різниця    Відношення")    
for i, t in enumerate(x):
    numheads[i] = np.sum(flips[:t])
    numtails[i] = t - numheads[i]
    diffs[i] = abs(numheads[i]-numtails[i])
    if numtails[i] == 0:
        k = 1
    else:
        k = numtails[i]
    ratios[i] = numheads[i]/k
    print('{:4} {:10} {:10} {:10} {:10}    {:<25}'.format(i,
                t, numheads[i], numtails[i], diffs[i], ratios[i]))

plt.subplot(2, 1, 1)                  #перший підграфік
plt.plot(x, diffs, 'ob', label = "Diff") #створити графік з легендою
plt.legend()
plt.subplot(2, 1, 2)                  #другий підграфік
plt.plot(x, ratios, 'or', label = "Ratio") #створити графік з легендою
plt.legend()
plt.show()

