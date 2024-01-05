class Cube():
    def __init__(self):
        self._a = 4
        self._b = 5
        self._c = 6
        
    def volume(self):
        return   self._a * self._b * self._c

c = Cube()

print(c.__dict__)
print(Cube.__dict__)

c.__dict__['new_atribute'] = 666

def volume1(self):
    return 555

c.__dict__['newMethod'] = volume1

print(c.newMethod(c))

#print(c.__dict__)


