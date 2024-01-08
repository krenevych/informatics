#t30_02_test_palindrome_v2.py
#Тестування функції, що перевіряє, чи є рядок паліндромом

import unittest
from t30_01_is_palindrome import *

class TestIsPalindrome(unittest.TestCase):
    "Клас містить тести для перевірки функції is_palindrome."
    def test_1_isempty(self):
        "1 - перевірити, чи є порожній рядок паліндромом"
        self.assertTrue(is_palindrome(''), "порожній рядок не є паліндромом")

    def test_2_iseven(self):
        "2 - перевірити, чи є рядок з парною кількістю символів паліндромом"
        self.assertTrue(is_palindrome('abba'), "abba не є паліндромом" )

    def test_3_isodd(self):
        "3 - перевірити, чи є рядок з непарною кількістю символів паліндромом"
        self.assertTrue(is_palindrome('aba'), "aba не є паліндромом")

    def test_4_iscase(self):
        "4 - перевірити, чи є рядок з різними регістрами літер паліндромом"
        self.assertTrue(is_palindrome('Aba'), "Aba не є паліндромом")

    def test_5_isdelim(self):
        "5 - перевірити, чи є рядок з розділювачами паліндромом"
        self.assertTrue(is_palindrome('Я несу гусеня!'),
                        "'Я несу гусеня!' не є паліндромом")

    def test_6_isnot(self):
        "5 - перевірити, чи не є несиметричний рядок"
        self.assertFalse(is_palindrome('abbd'), "abbd є паліндромом")

        
if __name__ == '__main__':
    unittest.main(verbosity=2)

