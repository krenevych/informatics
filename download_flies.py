from urllib.request import Request
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
import os


# Шаблон для знахолдження файлу розширення .py та .pyw та .pdf
FILEEXT = r'\"(.+(?:\.pyw*|\.pdf))\"'
SITE = r'https?:\/\/.*?(?=\/)'


def download_files(url, folder):
    """ Завантажує усі python-файли та pdf-файли за у директорію folder.
    """
    html = get_html(url)
    # Створюємо каталог для збереження файлів
    if not os.path.exists(folder):
        os.mkdir(folder)

    site = re.search(SITE, url, re.IGNORECASE).group()
    for file in re.findall(FILEEXT, html, re.IGNORECASE):
        fileurl = site + file              # Повне посилання на файл
        filename = os.path.basename(file)  # Визначаємо ім`я файлу
        print(fileurl)
        # Завантажуємо файл і зберігаємо їх у директорії folder
        urlretrieve(fileurl, os.path.join(folder, filename))


def get_html(url):
    """ Повертає розкодавані дані веб-сторінки за заданою адресою."""
    request = Request(url, headers={"User-Agent": "hello!"})
    response = urlopen(request)
    return str(response.read(), encoding="utf-8", errors="ignore")


rootSite = 'http://www.matfiz.univ.kiev.ua/pages/'
rootPath = "D:\\Repo\\informatics\\"

dirs = {
    '15': 'T01 - Лінійні програми',
    '16': 'T02 - Розгалужені програми',
    '17': 'T03 - Циклічні програми',
    '18': 'T04 - Числові типи даних',
    '20': 'T05 - Символи та рядки',
    '21': 'T06 - Списки',
    '22': 'T07 - Кортежі',
    '24': 'T08 - Словники',
    '25': 'T09 - Підпрограми',
    '26': 'T10 - Модулі та пакети',
    '27': 'T11 - Множини',
    '28': 'T12 - Файли',
    '29': 'T13 - ООП',
    '30': 'T14 - Рекурсивні структури даних',
    '31': 'T15 - Обробка виключень',
    '32': 'T16 - Ітератори та генератори',
    '33': 'T17 - Декоратори',
    '34': 'T18 - Множинне наслідування',
    '35': 'T19 - Метапрограмування',
    '36': 'T20 - Наукові обчислення',
    '37': 'Т21 - Регулярні вирази',
    '38': 'Т22 - Використання операційної системи',
    '39': 'Т23 - Робота з даними у офісних документах',
    '40': 'Т24 - Графічний інтерфейс',
    '41': 'Т25 - Загальна будова глобальних мереж',
    '42': 'Т26 - Побудова веб-клієнтів',
    '43': 'Т27 - Побудова веб-серверів',
    '44': 'Т28 - XML та JSON',
    '46': 'Т29 - Використання баз даних',
    '47': 'Т30 - Тестування. Розповсюдження власних застосувань',
}

if __name__ == "__main__":
    #webpage = input("webpage: ")
    #dirpath = input("dirpath: ")
    for page, dir in dirs.items():
        webpage = (rootSite + page).strip()
        dirpath = (rootPath + dir).strip()
        print(f"webpage: {webpage}")
        print(f"dirpath: {dirpath}")

        
        download_files(webpage, dirpath)
