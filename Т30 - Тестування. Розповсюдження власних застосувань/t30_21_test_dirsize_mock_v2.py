# t30_21_v2 Тестування функцій, що обчислюють розмір підкаталогів 
# Використання mock та patch у вигляді менеджера контексту

import unittest
from unittest.mock import patch
from T22.t22_01_dirsize_v1 import *

class TestDirSize(unittest.TestCase):
    "Клас містить тести для перевірки обчислення розміру підкаталогів."

    def test_1_dirsize_one(self):
        "1 - перевірити правильність обчислення розміру одного каталогу."
        with patch("T22.t22_01_dirsize_v1.os") as my_os:
            my_os.path.getsize.return_value = 2
            my_os.path.join.return_value = ""
            my_os.walk.side_effect = [[("dir", "", ["file1", "file2"])]]
            self.assertEqual(getdirsize("dir"), 4)

    def test_2__dirsize_all(self):
        "2 - перевірити правильність обчислення розміру усіх підкаталогів даного."
        with patch("T22.t22_01_dirsize_v1.os") as my_os:
            my_os.path.getsize.return_value = 2
            my_os.path.join = lambda x, y: y
            my_os.walk.side_effect = [ [("dir1", "", ["file1", "file2"])],
                             [("dir2", "", ["file1", "file2"]),
                                ("dir3", "", ["file3", "file4", "file5"])]]
            my_os.listdir.return_value = ["dir1", "dir2"]
            my_os.path.isdir.return_value = True
            self.assertEqual(getdirslist("dir"), [(10,"dir2"), (4, "dir1")])

         
if __name__ == '__main__':
    unittest.main(verbosity=2)

