#T23_01
# Видалення зайвих пропусків у документі MS Word

from docx import Document
import os


def delspaces(filename):
    '''Видаляє усі пропуски між словами у документі filename, окрім одного.

       Зберігає змінений документ з тим же ім'ям,
       до якого додається підкреслення '_'. 
    '''
    document = Document(filename)           # відкрити документ
    for paragraph in document.paragraphs:
        for run in paragraph.runs:
            text = run.text                 # отримати текст частини параграфа
            if text != '\n':                # щоб зберегти розриви сторінок
                lst = text.split(' ')           # розбити на список рядків пропусками
                # не можна використовувати text.split()
                # Після text.split(' ') утворяться порожні рядки там, де було декілька пропусків
                # їх не треба включати у список для побудови рядка-результата
                lstwos = [s for s in lst if s]  # список без порожніх елементів
                text = ' '.join(lstwos)         # текст з 1 пропуском між словами
                run.text = text                 # змінити текст частини параграфа

    fname, ext = os.path.splitext(filename) # розбити повне ім'я файлу
    fname += '_'
    newfilename = fname + ext               # додати до імені файлу підкреслення
    document.save(newfilename)              # зберегти документ
        
        
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:            # якщо не вистачає параметрів, ввести
        filename = input(".docx file name: ")
    else:
        filename = sys.argv[1]
    delspaces(filename)

