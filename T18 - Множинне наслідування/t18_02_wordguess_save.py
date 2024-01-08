#T18_02
#Відгадування слів з використанням кільцевого списку із записом результатів у файл

from T14.t14s2_12_wordguess import *
from t18_01_loadsaverlist import *

filename = '..\\T14\\' + filename #ім'я файлу зі словами
picklefile = 'saveddata.dat'      #ім'я файлу для збереження даних гри
glist = FileRlist(picklefile)     #створити новий об'єкт кільцевого списку
                                  #зі збереженням інформації


makeword(filename)          #вибрати слово з файлу для відгадування
ld = input('Завантажити гравців та результати попередньої гри?[y/n]').lower()[0]
if ld == 'y':
    glist.load()            #завантажити дані списку відгадувачів
    showguessers(glist)     #показати результати попередніх ігор
else:
    inputguessers(glist)    #ввести відгадувачів
play(glist)                 #здійснити відгадування 1 слова
print('Результати')
showguessers(glist)
ld = input('Зберегти гравців та результати попередньої гри?[y/n]').lower()[0]
if ld == 'y':
    glist.save()            #зберегти список відгадувачів з результатами гри


