# t15_42_sum_poly_v1.py
# Обчислення суми поліномів, які зберігаються у файлі у вигляді рядків

import random
from t15_41_polynome_ex import PolynomeEx, PolynomeError


def retrieve_polynome(s):
    """
    Функція обробляє 1 рядок файлу та перетворює його на поліном
    :param s: рядок
    :return: поліном
    """
    s = s.strip()
    p = PolynomeEx.fromstring(s)
    return p


def sum_poly(filename):
    """
    Функція обчислює суму поліномів, які зберігаються у файлі filename
    :param filename: ім'я файлу
    :return: сума поліномів (PolynomeEx)
    """
    f = open(filename, 'r')
    p = PolynomeEx()
    for line in f:
        p1 = retrieve_polynome(line)
        p = p + p1
    return p


filenames = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

for filename in filenames:
    p = sum_poly(filename)
    print("Сума поліномів у файлі '{}' дорівнює: {}".format(filename, p))
