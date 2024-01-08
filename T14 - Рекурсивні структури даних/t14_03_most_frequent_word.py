# Знаходження найчастішого слова у файлі
from collections import Counter

def most_frequent(filename):
    f = open(filename, 'r', encoding='windows-1251')
    # прочитати з файлу, перевести до нижнього регістру розбити на слова
    data = f.read().lower().split()
    f.close()

    # видалити символи-розділювачі
    data = map(lambda x: x.strip(".,-!?:;=\"'><"), data)
    # створити Counter тільки з непорожніх елементів
    cnt = Counter(filter(lambda x: x, data))
    return cnt.most_common(1)

filename = input("Ім'я файлу: ")
print("Найчастіше зустрічається", most_frequent(filename))
