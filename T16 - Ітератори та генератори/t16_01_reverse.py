#T16_01
#Простий ітератор Reverse

class Reverse:
    """Ітератор для проходження елементів послідовності у оберненому порядку."""

    def __init__(self, data):
        self._data = data           #_data - дані (послідовність)
        self._index = len(data)     #_index - індекс поточного елемента послідовності

    def __iter__(self):
        """Метод __iter__ повертає сам об'єкт як ітератор."""
        return self

    def __next__(self):
        """Метод __next__ повертає наступний елемент послідовності у порядку слідування."""
        if self._index == 0:        #якщо дійшли до кінця послідовності
            raise StopIteration     #ініціювати виключення
        self._index = self._index - 1
        return self._data[self._index]
