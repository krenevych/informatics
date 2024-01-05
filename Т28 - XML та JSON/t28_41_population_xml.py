#T28_41
#Оцінка змін населення країн за період за даними Світового Банку. XML

import xml.etree.ElementTree as et
import zlib
from urllib.request import urlopen
from urllib.parse import urlencode

def get_page(url_params):
    """Функція читає одну сторінку документу з url_params.

       Повертає рядок - сторінку документу.
    """
    request = urlopen(url_params) # відправка запиту
#    print(request.status, request.headers)
    # отримати відповідь сервера
    if request.getheader("Content-Encoding"): # якщо дані заархівовано
        data_zipped = request.read()
        data = zlib.decompress(data_zipped, zlib.MAX_WBITS | 16) # magic :)
    else:
        data = request.read()
    data = data.decode('utf-8')
    request.close()
#    print("data=", data)
    return data
    

def multipage_reader(url, page_proc_func, **params):
    """Функція читає багатосторінковий документ з url з параметрами params.

       page_proc_func - функція, яка обробляє одну сторінку xml.
       Кожна сторінка документу повинна мати заголовок - елемент XML -
       та список елементів-значень.
       Заголовок, зокрема, повинен містити атрибут - кількість сторінок ("pages").
    """
    if params:
        query = urlencode(params, encoding='utf-8') # формування рядка параметрів
        url_params = url + '?' + query
    else:
        params = {}
        url_params = url
    data = get_page(url_params)             # отримати сторінку з даними
    response = et.fromstring(data)          # перетворити дані у XML
    page_proc_func(response)                # обробити першу сторінку
    page_num = int(response.get("pages"))   # обчислити кількість сторінок
    print('url {} page {} of {}'.format(url, 1, page_num))
    for page in range(2, page_num + 1):
        params["page"] = str(page)
        query = urlencode(params, encoding='utf-8') # формування рядка параметрів 
        url_params = url + '?' + query
        data = get_page(url_params)                 # отримати сторінку з даними
        response = et.fromstring(data)              # перетворити дані у XML
        page_proc_func(response)                    # обробити сторінку
        print('url {} page {} of {}'.format(url, page, page_num))
        
COUNTRIES_URL = "http://api.worldbank.org/countries"
POPULATION_URL = "http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL"
WB = "{http://www.worldbank.org}"

class PopulationXML:
    '''Клас для визначення списку країн з змінами населення за період
       за даними Світового Банку з використанням XML.

       Поля:
        self.countries - словник країн. Ключ - двохсимвольний код країни.
                         Дані - список кортежів з назви країни та населення у
                         початковому та кінцевому роках
        self.pop_change - список кортежів (<зміна населення>, <код країни>, <назва>)
        self_start_year - початковий рік
        self.fin_year   - кінцевий рік
        self.list_index - індекс у списку для населення країни
                          (початковий рік - 1, кінцевий рік - 2)
    '''
    def __init__(self, start_year, fin_year):
        self.countries = {}
        self.pop_change = []
        self.start_year = start_year
        self.fin_year = fin_year
        
    def evaluate_changes(self):
        '''Оцінює зміни населення.'''
        # Будує словник країн
        multipage_reader(COUNTRIES_URL, self.process_countries_page)
#        print(self.countries) 
        # Будує список кортежів (<зміна населення>, <код країни>, <назва>)
        self.list_index = 1
        multipage_reader(POPULATION_URL, self.process_population_page,
                         date=self.start_year)
        self.list_index = 2
        multipage_reader(POPULATION_URL, self.process_population_page,
                         date=self.fin_year)
        for country, c_list in self.countries.items():
            if c_list[1] and c_list[2]:
                coeff = c_list[2] / c_list[1]
                self.pop_change.append((coeff, country, c_list[0]))
        self.pop_change.sort(reverse=True)
#        print(self.countries) 
        return self.pop_change

    def process_countries_page(self, response):
        '''Обробляє сторінку з даними про країни, будує словник країн.'''
        page_countries = {}
        for country in response.findall(WB + 'country'):
            key = country.find(WB + "iso2Code").text
            c_name = country.find(WB + "name").text
            region = country.find(WB + "region").text
            if region != "Aggregates":
                page_countries[key] = [c_name, 0, 0]
        self.countries.update(page_countries)

    def process_population_page(self, response):
        '''Обробляє сторінку з даними про населення, змінює словник країн.

           Заносить дані про населення у відповідний елемент списку для кожної країни.
           Індекс елемента задає self.list_index (1 або 2)
        '''
        for data in response.findall(WB + "data"):
            country_id = data.find(WB + "country").get("id")
            population = data.find(WB + "value").text
#            print(country_id, population)
            if country_id in self.countries and population:
                self.countries[country_id][self.list_index] = int(population)

            
START_DEFAULT = 1995
FIN_DEFAULT = 2015

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1:
        start = START_DEFAULT
        fin = FIN_DEFAULT
    else:
        start = sys.argv[1]
        fin = sys.argv[2]

    p_xml = PopulationXML(start, fin)
    result = p_xml.evaluate_changes()
    print("\nПеріод: {} - {}".format(start,  fin))
    ten = min(len(result), 10)
    print('10 перших країн за зростанням (зменшенням) населення')
    for i in range(ten):
        print('{:40} {:.2f}'.format(result[i][2], result[i][0]))

    print('\n10 останніх країн за зростанням (зменшенням) населення')
    for i in range(-ten, 0):
        print('{:40} {:.2f}'.format(result[i][2], result[i][0]))

