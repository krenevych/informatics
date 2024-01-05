#T28_21
#Телефонний довідник (xml)
import xml.etree.ElementTree as et

class XMLRefBook:
    '''Клас для ведення телефонного довідника з використанням XML.

       У файлі XML записи довідника зберігаються у форматі:
       <refbook>
           <friend name="ім'я"> телефон <friend>
          ...
       </refbook>

       Поля:
       self.filename - ім'я файлу довідника
    '''
    def __init__(self, filename):
        self.filename = filename

        
    def createrb(self):
        '''Створює довідник та записує у нього n записів.'''
        n = int(input('Кількість записів: '))
        book = et.Element('refbook')        # створити кореневий вузол дерева
        for i in range(n):
            friend = et.Element('friend')   # створити вузол дерева
            name = input('Прізвище: ')
            friend.set('name', name)        # встановити значення атрибута
            phone = input('Телефон: ')
            friend.text = phone             # змінити текст вузла
            book.append(friend)             # додати сина (вузол)
        e = et.ElementTree(book)            # створити документ
        e.write(self.filename)              # зберегти файл

    def apprb(self):
        '''Доповнює довідник одним записом.'''
        # завантажити та проаналізувати документ
        e = et.parse(self.filename)        
        book = e.getroot()
        friend = et.Element('friend')       # створити вузол дерева
        name = input('Прізвище: ')
        friend.set('name', name)            # встановити значення атрибута
        phone = input('Телефон: ')
        friend.text = phone                 # змінити текст вузла
        book.append(friend)                 # додати сина (вузол)
        e.write(self.filename)              # зберегти файл

    def searchrb(self, name):
        '''Шукає у довіднику телефон за ім'ям name.

        Якщо не знайдено, повертає порожній рядок.
        '''
        # завантажити та проаналізувати документ
        e = et.parse(self.filename)
        phone = ""
        # знайти всі вузли "friend"
        for friend in e.iterfind('friend'):
            if friend.get('name') == name:
                phone = friend.text
                break
        return phone
        
    def replacerb(self, name, newphone):
        '''Замінює у довіднику телефон за ім'ям name на newphone.

        Якщо не знайдено, нічого не робить.
        '''
        # завантажити та проаналізувати документ
        e = et.parse(self.filename)
        phone = ""
        # знайти всі вузли "friend"
        for friend in e.iterfind('friend'):
            if friend.get('name') == name:
                friend.text = newphone
                break
        e.write(self.filename)
      

        
    
filename = 'refs.xml'      #ім'я файлу довідника

rb = XMLRefBook(filename)

while True:
    k = int(input('Режим роботи [1 - 5]:'))
    if k == 1:                      #створити довідник 
        rb.createrb()
    elif k == 2:                    #додати запис до довідника 
        rb.apprb()
    elif k == 3:                    #знайти телефон у довіднику
        name = input('Прізвище: ')
        phone = rb.searchrb(name)
        if len(phone) > 0:
            print('Телефон:', phone)
        else:
            print('не знайдено')
    elif k == 4:                    #замінити телефон у довіднику 
        name = input('Прізвище: ')
        phone = input('Новий телефон: ')
        rb.replacerb(name, phone)
    elif k == 5:
        break
        





      


