#T09s2_11
#Ханойські вежі

def hanoi (n,a,b,c):
    if n != 0:
        hanoi(n-1,a,c,b)
        print('{} -> {}'.format(a,b))
        hanoi(n-1,c,b,a)

n = int(input("введіть кілкість дисків: "))

hanoi(n,1,2,3)





