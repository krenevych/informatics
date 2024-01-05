import sys

fName = 'myfile.txt'

fName = sys.argv[1]



f = open(fName, 'r')

for line in f:
    print(line, end = "")

f.close()
