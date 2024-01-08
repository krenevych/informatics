# Обчислення частоти входження слова у послідовність слів
from collections import defaultdict

def count_words():
    d = defaultdict(int)

    print("Вводьте слова. Завершення - ''")    
    while True:
        w = input("? ")
        if not w:
            break
        d[w] += 1

    return d

d = count_words()
for w in d:
    print(w, d[w])

