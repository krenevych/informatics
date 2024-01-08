# t15_41_polynome_ex.py
# Поліном. Обробка виключень

from T14.t14_20_polynome import Polynome

class PolynomeError(Exception):
    """
    Клас виключення для поліномів
    """
    def __str__(self):
        return "Помилка обробки поліному"


class PolynomeEmptyError(PolynomeError):
    """
    Клас виключення порожнього поліному (порожнього рядка)
    """
    def __str__(self):
        return "Порожній рядок для поліному"


class PolynomeCoeffError(PolynomeError):
    """
    Клас виключення недопустимого коефіцієнту поліному
    """
    def __init__(self, coeff):
        self.coeff = coeff          # значення коефіцієнту,
                                    # що викликало помилку

    def __str__(self):
        return "Недопустимий коефіцієнт: {}".format(self.coeff)


class PolynomeDegreeError(PolynomeError):
    """
    Клас виключення недопустимої степені поліному
    """
    def __init__(self, degree):
        self.degree = degree        # значення степені,
                                    # що викликало помилку

    def __str__(self):
        return "Недопустима степінь: {}".format(self.degree)


class PolynomeEx(Polynome):
    """Даний клас є нащадком Polynome та реалізує дії над поліномами.

    Клас ініціює виключення при неправильному завданні поліному
    за допомогою рядка
    або при неправильному додаванні одночлена до поліному
    """
    def fromstring(s):
        """
        Перетворення рядка у поліном.

        Рядок повинен мати вигляд (наприклад):

        3.7*x**3 + 0.3*x**1 + -1.2*x**0

        Пробіли між коефіцієнтами та степенями не допускаються.
        Від'ємні коефіцієнти записувати як у прикладі вище.
        У разі виникнення помилки, ініціює відповідне виключення
        :param s: рядок
        :return: об'єкт класу Polynome
        """
        p = Polynome()
        s = s.replace('+',' ')
        ls = s.split()  #розбиваємо на список одночленів
        if not ls:
            raise PolynomeEmptyError

        for m in ls:
            c = m.split('*x**') #виділяємо степінь та коефіцієнт
            try:
                k = int(c[1])
                if k < 0:
                    raise PolynomeDegreeError(k)
            except ValueError:
                raise PolynomeDegreeError(c[1])
            try:
                v = float(c[0])
            except ValueError:
                raise PolynomeCoeffError(c[0])
            p[k] = v
        return p

    fromstring = staticmethod(fromstring)

    def add_monom(self, deg, coeff):
        """
        Додати одночлен степені deg до поліному.
        У разі виникнення помилки, ініціює відповідне виключення
        :param deg: степінь одночлена
        :param coeff: коефіцієнт одночлена
        :return: None
        """
        try:
            coeff = float(coeff)
        except ValueError:
            raise PolynomeCoeffError(coeff)

        if coeff != 0:
            try:
                deg = int(deg)
                if deg < 0:
                    raise PolynomeDegreeError(deg)
            except ValueError:
                raise PolynomeDegreeError(deg)
            self[deg] += coeff
