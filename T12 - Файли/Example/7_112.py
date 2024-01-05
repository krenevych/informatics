
def readCoefFromFile(aFileName):
    fCoef = open(aFileName, 'r')
    listCoef = []
    for line in fCoef:
        listCoef.append(float(line))
    fCoef.close()
    return listCoef

lCoef = readCoefFromFile('coef.txt')

x = float(input('x = '))

xn = 1.0
f = 0

for a in lCoef:
    f += a * xn
    xn *= x

print(f)






    
