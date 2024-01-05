#T23_21
# Злиття даних з файлів MS Word, MS Excel за шаблоном MS Word
# Імена полів, що заповнюються даними, мають бути взяті у фігурні дужки { }
# Файли, з яких треба брати дані, вказують у конфігураційному файлі
# Клас MergeSource

from openpyxl import *
from docx import Document
import os

from t23_22_sourceitem import *
                
class MergeSource:
    '''Джерела даних для злиття.

       Призначено для під'єднання до джерел даних та повернення даних по кроках.
       self.lead - ім'я поля, яке є провідним параметром
       self.fields - словник, що має ключами імена полів, а значеннями -
                     об'єкти класу SourceItem
       Клас підтримує ітераційний протокол.
    '''

    def __init__(self, param_files, leadparam):
        '''Конструктор.

           Здійснює під'єднання до джерел даних.
           param_files - словник, що містить імена параметрів (полів)
           та імена файлів, де розташовано відповідні дані.
           leadparam - провідний параметр.
           Кількість записів даних розраховується за цим параметром.
        '''
        self.lead = leadparam
        self.fields = {}
        openfiles = {}      # словник, що містить фмена файлів та відповідні
                            # об'єкти документ (Document) або робоча книга (Workbook)
        for name in param_files:
            filename = param_files[name]
            base, ext = os.path.splitext(filename) # визначаємо тип джерела даних
            if ext == '.xlsx':
                typ = 'excel'
            else:
                typ = 'word'
            if filename not in openfiles:  # якщо файл не відкрито, відкриваємо
                # rootobj - це документ (Document) або робоча книга (Workbook)
                if typ == 'excel':
                    rootobj = load_workbook(filename)
                else:
                     rootobj = Document(filename)
                openfiles[filename] = rootobj 
            else:
                rootobj = openfiles[filename]
            islead = (name == leadparam)
            # створюємо новий об'єкт SourceItem та запам'ятовуємо у словнику self.fields
            self.fields[name] = SourceItem(name, typ, rootobj, islead)

    def __iter__(self):
        '''Повертає об'єкт-ітератор.

           Метод для підтримки ітераційного протоколу
        '''
        return self

    def __next__(self):
        '''Повертає наступний запис з даними для злиття.

           Метод для підтримки ітераційного протоколу.
           Запис - це словник з ключами-іменами полів та
           значеннями - об'єктами класу SourceItem.
        '''
        mergerecord = {}
        for name, srcitem in self.fields.items():
            # тут може виникнути виключення StopIteration
            srcitem.next() # перейти до наступного запису
            mergerecord[name] = srcitem
        return mergerecord
                
           
