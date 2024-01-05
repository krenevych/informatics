
class MyIter:

    def __init__(self, data):
        self._data = data
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current != len(self._data):
            num = self._current
            self._current += 1
            return self._data[num]
        else:
            raise StopIteration

myData = list(range(10, -1, -1))
print(myData)

it = MyIter(myData)


while True:
    try:
        print (next(it))
    except StopIteration:
        break

        
