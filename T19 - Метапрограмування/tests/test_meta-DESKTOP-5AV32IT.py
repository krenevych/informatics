
class Cube():
    def __init__(self):
        self._a = 4
        self._b = 5
        self._c = 6
        
    def volume(self):
        return   self._a * self._b * self._c


c = Cube()
#print(c.volume())
#print(c.volume1())


def volume1(self):
    return   111

Cube = type("Cube", (Cube,), {'volume1' : volume1})

c1 = Cube()
print(c1.volume())
print(c1.volume1())

