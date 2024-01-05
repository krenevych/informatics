#T21_01_v2
#Побудова списку років, що є у текстовому файлі
#Збереження позиції у рядку та позиції відносно початку файлу

import re

P_YEAR = r'\b\d{3,4}\b'

def extract_years_from_file(fname):
    '''Обробляє файл fname з відомостями про дати подій (роки)

    '''
    years = []                          # список років
    offset = 0                          # зсув початку рядка у файлі
    f = open(fname,"r")
    for i, line in enumerate(f,1):
        extract_years_from_line(line, i, offset, years) # обробити 1 рядок файлу
        offset +=len(line)
    f.close()
    return years

def extract_years_from_line(line, line_number, offset, years):
    '''Обробляє рядок line з файлу з відомостями про дати подій (роки)

    Додає рік та номер рядка файлу line_number,
    де зустрічається цей рік, до списку years.
    '''
    years_it = re.finditer(P_YEAR, line)    # знайти усі роки у рядку
    for m in years_it:
        ly = m.group()                      # знайдений рік
        pos = m.start()                     # позиція у рядку
        # додаємо до списку кортеж
        # (<рік>, <номер рядка> <позиція> <зсув у файлі>)
        years.append((ly, line_number, pos, offset + pos))     
    
    
if __name__ == '__main__':
    #filename = input("Ім'я файлу: ")
    filename = 'france17.txt'
    years = extract_years_from_file(filename)
    years.sort()        # впорядковуємо по роках
    for y in years:
        print(y)
