#T09s1_21
#Визначення символа, який входить у рядок найбільшу кількість разів,
# а також кількості входжень

def max_char (s):
    '''Визначає символ, який входить у рядок s найбільшу кількість разів, а також кількість входжень.

    '''
    mx = 0
    mc = chr(0)
    if len(s) > 0:
        mx, mc = max([(s.count(c), c) for c in s])
    return mc, mx


s = input("введіть рядок: ")

c, n = max_char(s)

k = n % 10
kk = n % 100
if k in range(5,10) or k == 0 or kk in range(11,20):
    suf = "ів"
elif k in range(2,5):
    suf = "и"
else:   #k == 1
    suf = ""

print("Символ '{}' входить у рядок {} раз{}".format(c, n, suf))
    




