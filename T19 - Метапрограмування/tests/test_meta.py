from abc import abstractmethod, ABCMeta

#class Figure():
class Figure(metaclass = ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def square(self):
        pass

class Cube(Figure):
    def __init__(self):
        self._a = 4
        self._b = 5
        self._c = 6
        
    def square(self):
        return   self._a * self._b * self._c

#f = Figure()
#print(f.square())

def volume(self):
    return  111

aaa = type("Cube", (Cube,), {'volume' : volume})
c1 = aaa()





print (c1.__dict__)

print(c1.volume())
#print(c1.square())

