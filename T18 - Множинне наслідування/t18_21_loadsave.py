#T18_21
#Приклад множинного наслідування
#Клас, який наслідує від WordGuessGame та класу збереження/читання даних класу
#LoadSave взято з "Саммерфилд. Программирование на Python 3." 

from t18_22_wordguess import *
import pickle

class LoadSave:
    '''Клас, який зберігає дані з атрибутів класу-нащадка
    '''
    def __init__(self, filename, *attribute_names):
        '''Конструктор збирає у список імена атрибутів.

        Проводить перейменування атрибутів, якщо потрібно (починаються з __).
        '''
        self.filename = filename        #ім'я файлу для збереження даних
        self.__attribute_names = []     #список імен атрибутів, які будуть збережені
        for name in attribute_names: 
            if name.startswith("__"): 
                name = "_" + self .__class__.__name__ + name 
            self.__attribute_names.append(name)

    def save(self): 
        '''Зберігає дані у файлі.

        '''
        with open(self.filename, "wb") as fh: 
            data = []                            #список значень атрибутів
            for name in self.__attribute_names: 
                data.append(getattr(self, name)) #додати значення атрибуту до списку
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL) #зберегти список

    def load(self): 
        '''Читає дані з файлу.

        '''
        with open(self.filename, "rb") as fh: 
            data = pickle.load(fh) #прочитати збережений список
            for name, value in zip(self.__attribute_names, data):
                setattr(self, name, value) #змінити значення атрибуту
 
class FileWordGuessGame(WordGuessGame, LoadSave):
    '''Клас, який успадковує від Rlist, LoadSave
    '''
    def __init__(self, words_file, filename, guessers=None):
        WordGuessGame.__init__(self, words_file, guessers)
        LoadSave.__init__(self, filename, "guessers", "_word",
                          "_guessed", "_gameover")

