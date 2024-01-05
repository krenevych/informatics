f = open('f.txt', 'r')

s = f.readline();
l = s.split()
print(l)
f.close()

lp = []
lnp = []
for x in l:
    if int(x) % 2 == 0:
        lp.append(x)
    else:
        lnp.append(x)

print(lp)
print(lnp)

g = open('g.txt', 'w')
h = open('h.txt', 'w')

for x in lp: 
    g.write(x + ' ')

for x in lnp: 
    h.write(x + ' ')

g.close()
h.close()









