#t27_22_testio.py
#Класи введення-виведення тестів.

from abc import ABCMeta, abstractmethod
from t27_21_quiz import *

class TestIO(metaclass = ABCMeta):
    """Абстрактний клас введення тестів та виведення результатів.

        self.quissuite - тести (об'єкт класу QuisSuite)
        self.urn - розташування ресурсу з тестами (файл або база даних)
        self.params - додаткові параметри для читання тестів
        self.users - список користувачів - кортежів (користувач, пароль)
        self.results = список результатів - кортежів Result
    """

    def __init__(self, quissuite, urn, **params):
        self.quissuite = quissuite
        self.urn = urn
        self.params = params
        self._users = []
    
    @abstractmethod
    def read(self):
        """Читати тести.
           Повертає список об'єктів класу Quiz та список результатів"""
        pass

    @property
    @abstractmethod
    def users(self):
        "Повертає список кортежів (користувач, пароль)"
        pass

    @abstractmethod
    def writeresult(self, result):
        "Писати результат тесту з result."
        pass

        


        

