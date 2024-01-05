from t14s1_21_deque import *
import random

class Passenger:
    def __init__(self, aNamePassenger):
        self._namePassenger = aNamePassenger
        self._weightLuggage = 0.0
        self._numThings = 0
    def setLuggage(self, aWeightLuggage, aNumThings):
        self._weightLuggage = aWeightLuggage
        self._numThings = aNumThings
    def getLuggage(self):
        return self._weightLuggage, self._numThings
    def getName(self):
        return self._namePassenger

    
passengers = Deque()
numberOfPass = random.randint(5, 6)
for i in range(numberOfPass):
    name = "Passenger " + str(i)
    pas = Passenger(name)
    c = random.randint(0, 20)
    w = 10.0 + 100.0 * random.random()
    pas.setLuggage(w, c)
    passengers.puten(pas)

passengers2 = clone(passengers)
while not passengers2.isempty():
    pas = passengers2.getbg()
    print(pas.getName(), pas.getLuggage())
        
print("=======================")

passengers2 = clone(passengers)
totalW = 0.0
totalNumPas = 0
while not passengers2.isempty():
    pas = passengers2.getbg()
    totalNumPas += 1
    totalW += pas.getLuggage()[0]

if totalNumPas > 0:
    avWeight = totalW / totalNumPas;
else:
    avWeight = 0;

numPassMoreThanAv = 0;
passengers2 = clone(passengers)
while not passengers2.isempty():
    pas = passengers2.getbg()
    if (pas.getLuggage()[0] > avWeight ):
        numPassMoreThanAv += 1

print ("Number of passengers with weigth more than avarage (%f) is %d" %(avWeight, numPassMoreThanAv))    




