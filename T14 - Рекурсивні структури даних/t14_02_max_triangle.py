# Обчислення трикутника максимальної довжини
from t14_01_triangle import Point2, Segment, Triangle

def input_point(name):
    print("Введіть точку {}".format(name))
    str_xy = input("(x, y) = ")
    lst_xy = str_xy.strip("()").split(",")
    x, y = map(float, lst_xy)
    return Point2(x, y)

def _is_valid_triangle(a, b, c):
    s1 = Segment(a, b).len()
    s2 = Segment(b, c).len()
    s3 = Segment(a, c).len()
    return s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2

def input_triangle(m):
    while True:
        print("Введіть трикутник {}".format(m))
        a = input_point("a")
        b = input_point("b")
        c = input_point("c")
        if _is_valid_triangle(a, b, c):
            break
        print("Точки {}, {}, {} не утворюють трикутник".format(a, b, c))

    return Triangle(a, b, c)


if __name__ == "__main__":
    while True:
        n = int(input("Кількість трикутників (>0): "))
        if n > 0:
            break

    triangles = []
    for i in range (n):
        triangles.append(input_triangle(i + 1))

    max_p = max_s = 0
    k_p = k_s = 0
    for i, t in enumerate(triangles):
        if t.perimeter() > max_p:
            max_p = t.perimeter()
            k_p = i

        if t.square() > max_s:
            max_s = t.square()
            k_s = i

    print("Трикутник з максимальним периметром", triangles[k_p])
    print("Трикутник з максимальною площею", triangles[k_s])
