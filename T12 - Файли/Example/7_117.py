def listFib(aN):
    f0 = 1; f1 = 1; res = [f0, f1]
    while f1 < aN:
        f = f0 + f1
        f0 = f1
        f1 = f
        if f > aN:
            break
        res.append(f)
    return res

n = int (input('n = '))
l = listFib(n)

f = open('list_fib.txt', 'w')
for curFib in l:
    f.write(str(curFib) + '\n')
f.close()









        
