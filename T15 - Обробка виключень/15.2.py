check = True

while check == True:
    try:
        x = float(input("Enter x (|x| < 1):"))
        assert abs(x) < 1, "|x| >= 1"
    except ValueError:
        print("Введите число |x| < 1")
    except AssertionError:
        print("Введите число |x| < 1")
    else:
        check = False

k = 1
el = x
y = x
yprev = 0
eps = 0.000001
while abs(y - yprev) > eps:
    k += 1
    el = (el * x * (-1))/k
    yprev = y
    y = y + el
print("Ln({}) = {}" .format(x+1, y))



