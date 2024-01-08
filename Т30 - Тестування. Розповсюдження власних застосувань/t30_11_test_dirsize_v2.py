#t30_11_test_dirsize_v2.py
# Тестування для порожнього та непорожнього підкаталогу

import os
import shutil
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

class TestNotEmptyDirSize(unittest.TestCase):
    "Клас містить тести для перевірки обчислення розміру підкаталогів."
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.size = 0           # розмір одного каталогу
        self.result = []        # список каталогів разом з їх розмірами
        self.minbytes = 3       # мінімальний розмір файлу

    def _write_one_file(self, fname, bytes_num):
        "Записати один файл з ім'ям fname та кількістю байтів bytes_num."
        with open(fname, "wb") as f:
            to_write = bytes(list(range(bytes_num)))
            f.write(to_write)
            self.size += bytes_num

    def _make_one_dir(self, dirname, files_num):
        "Створити один каталог з ім'ям dirname та кількістю файлів files_num."
        os.mkdir(dirname)
        for i in range(files_num):
            fname = "{}/file{}".format(dirname, i)
            self._write_one_file(fname, self.minbytes + i)
        
    def setUp(self):
        "Встановлення тестового оточення."
        # створити підкаталог _test
        self._make_one_dir("_test", 0)
        # створити підкаталог _test/dir1 з 2 файлами
        self.size = 0 
        dirname = "_test" + os.sep + "dir1"
        self._make_one_dir(dirname, 2)
        # створити підкаталог _test/dir1/subdir1 з 3 файлами
        self._make_one_dir(dirname + os.sep + "subdir1", 3)
        self.result.append((self.size, dirname))
        # створити підкаталог _test/dir2 з 1 файлом
        self.size = 0
        dirname = "_test" + os.sep + "dir2"
        self._make_one_dir(dirname, 1)
        self.result.append((self.size, dirname))
        # впорядкувати список каталогів за незростанням розміру
        self.result.sort(reverse = True)

    def tearDown(self):
        "Очищення тестового оточення."
        shutil.rmtree("_test")

    def test_1_dirsize_one(self):
        "1 - перевірити правильність обчислення розміру одного каталогу"
        self.assertEqual(getdirsize("_test" + os.sep + "dir2"), self.minbytes)

    def test_2__dirsize_all(self):
        "2 - перевірити правильність обчислення розміру усіх підкаталогів даного"
        self.assertEqual(getdirslist('_test'), self.result)


         
if __name__ == '__main__':
    unittest.main(verbosity=2)

