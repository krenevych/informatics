#t30_01_is_palindrome.py
#Функція, що перевіряє, чи є рядок паліндромом

import re


def is_palindrome(string):
    '''Перевіряє, чи є рядок string паліндромом.'''
    # видалити всі символи-розділювачі
    string = re.sub(r'''[ !?.,+:;"'()\-]+''', '', string)
    string = string.lower() # перевести до нижнього регістру
#    print(string)
    return string == string[::-1]
