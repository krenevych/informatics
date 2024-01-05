#T21_01_v1
#Побудова списку років, що є у текстовому файлі

import re

P_YEAR = r'\b\d{3,4}'

def extract_years_from_file(fname):
    '''Обробляє файл fname з відомостями про дати подій (роки)

    '''
    years = []                          # список років
    f = open(fname,"r")
    for i, line in enumerate(f,1):
        extract_years_from_line(line, i, years)    # обробити 1 рядок файлу
    f.close()
    return years

def extract_years_from_line(line, line_number, years):
    '''Обробляє рядок line з файлу з відомостями про дати подій (роки)

    Додає рік та номер рядка файлу line_number,
    де зустрічається цей рік, до списку years.
    '''
    line_years = re.findall(P_YEAR, line)   # знайти усі роки у рядку
    for ly in line_years:
        years.append((ly, line_number))     # додаємо до списку кортеж
                                            # (<рік>, <номер рядка>)
    
    
if __name__ == '__main__':
  #  filename = input("Ім'я файлу: ")
    filename = 'france17.txt'
    years = extract_years_from_file(filename)
    years.sort()        # впорядковуємо по роках
    for y in years:
        print(y)
