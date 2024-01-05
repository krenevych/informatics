from urllib.request import Request
from urllib.request import urlopen
from urllib.request import urlretrieve
import re
import os


# Шаблон для знахолдження файлу розширення .py та .pyw та .pdf
FILEEXT = r'\"(.+(?:\.pyw*|\.pdf))\"'


def download_files(url, folder):
    """ Завантажує усі python-файли та pdf-файли за у директорію folder.
    """
    html = get_html(url)
    # Створюємо каталог для збереження файлів
    if not os.path.exists(folder):
        os.mkdir(folder)

    for example in re.findall(FILEEXT, html, re.IGNORECASE):
        example_url = url + example           # Повне посилання на файл
        filename = os.path.basename(example)  # Визначаємо ім`я файлу
        # print(filename)
        # Завантажуємо файл і зберігаємо їх у директорії folder
        urlretrieve(example_url, os.path.join(folder, filename))


def get_html(url):
    """ Повертає розкодавані дані веб-сторінки за заданою адресою."""
    request = Request(url, headers={"User-Agent": "hello!"})
    response = urlopen(request)
    return str(response.read(), encoding="utf-8", errors="ignore")


if __name__ == "__main__":
    #webpage = input("webpage: ")
    #dirpath = input("dirpath: ")
    webpage = """
http://www.matfiz.univ.kiev.ua/pages/47
    """.strip()
    
    dirpath = r"""
D:\Repo\informatics\Т30 - Тестування. Розповсюдження власних застосувань
    """.strip()
    download_files(webpage, dirpath)
