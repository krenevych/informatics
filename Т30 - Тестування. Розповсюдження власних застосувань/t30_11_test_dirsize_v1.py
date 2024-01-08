#t30_11_test_dirsize_v1.py
# Тестування для порожнього підкаталогу

import os
import unittest
from T22.t22_01_dirsize_v1 import *

class TestEmptyDirSize(unittest.TestCase):
    "Клас містить тести для перевірки обчислення розміру підкаталогів."
    def setUp(self):
        "Встановлення тестового оточення."
        os.mkdir("_test")

    def tearDown(self):
        "Очищення тестового оточення."
        os.rmdir("_test")

    def test_1_dirsize_one(self):
        "1 - перевірити правильність обчислення розміру одного каталогу"
        self.assertEqual(getdirsize('_test'), 0)

    def test_2__dirsize_all(self):
        "2 - перевірити правильність обчислення розміру усіх підкаталогів даного"
        self.assertEqual(getdirslist('_test'), [])

         
if __name__ == '__main__':
    unittest.main(verbosity=2)

