#T18_23
#Відгадування слів з використанням деку із записом результатів у файл

from collections import deque

from t18_22_wordguess import *
from t18_21_loadsave import *

filename = 'text.txt' #ім'я файлу зі словами
picklefile = 'saveddata.dat'      #ім'я файлу для збереження даних гри

ld = input('Завантажити гравців та результати попередньої гри?[y/n]').lower()[0]
if ld == 'y':
    game = FileWordGuessGame(filename, picklefile)
    game.load()            #завантажити дані списку відгадувачів
    showguessers(game.guessers)    #показати результати попередніх ігор
else:
    guessers = deque()
    inputguessers(guessers)    #ввести відгадувачів
    game = FileWordGuessGame(filename, picklefile, guessers)

try:
    game.play()                 #здійснити відгадування 1 слова
except KeyboardInterrupt:
    ld = input('Зберегти гравців та результати попередньої гри?[y/n]').lower()[0]
    if ld == 'y':
        game.save()            #зберегти список відгадувачів з результатами гри
 
print('Результати')
showguessers(game.guessers)


