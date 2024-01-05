# t30_21_v1 Тестування функцій, що обчислюють розмір підкаталогів 
# Використання mock та patch

import unittest
from unittest.mock import patch
from T22.t22_01_dirsize_v1 import *

def my_join(directory, dir):
    "Тимчасова реалізація os.path.join."
    return dir

def my_walk(dir):
    "Тимчасова реалізація os.walk."
    if dir == "dir1":
        return [("dir1", "", ["file1", "file2"])]
    else:
        return [("dir2", "", ["file1", "file2"]),
                                   ("dir3", "", ["file3", "file4", "file5"])]


class TestDirSize(unittest.TestCase):
    "Клас містить тести для перевірки обчислення розміру підкаталогів."

    @patch("T22.t22_01_dirsize_v1.os")
    def test_1_dirsize_one(self, my_os):
        "1 - перевірити правильність обчислення розміру одного каталогу"
        my_os.path.getsize.return_value = 2
        my_os.path.join.return_value = ""
        my_os.walk.return_value = [("dir", "", ["file1", "file2"])]
        self.assertEqual(getdirsize("dir"), 4)

    @patch("T22.t22_01_dirsize_v1.os")
    def test_2__dirsize_all(self, my_os):
        "2 - перевірити правильність обчислення розміру усіх підкаталогів даного"
        my_os.path.getsize.return_value = 2
        my_os.path.join = my_join
        my_os.walk = my_walk
        my_os.listdir.return_value = ["dir1", "dir2"]
        my_os.path.isdir.return_value = True
        self.assertEqual(getdirslist("dir"), [(10,"dir2"), (4, "dir1")])

         
if __name__ == '__main__':
    unittest.main(verbosity=2)

