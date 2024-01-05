

def pow_x_n():
    x = 2
    n = 0
    res = 1
    while True:
        yield res
        n+=1
        res *= x

n = 5
x_n = pow_x_n()

for i in range(n):
    print(next(x_n))

i = 0
for x in pow_x_n():
    print(x)
    i+=1;
    if i > n:
        break
        
