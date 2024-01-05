#T06_11_v1
#Обчислення мінімального елемента матриці

n = int(input("Enter number of rows of matrix "))
m = int(input("Enter number of columns of matrix "))

A = []
for i in range(n):
    A.append(list())
    for j in range(m):
        s = "A[" + str(i)  + "," + str(j) + "] = "
        a = float(input(s))
        A[i].append(a)

for i in range(n):
    for j in range(m):
        print("%3f  " %(A[i][j]), end = " ")
    print()

min = A[0][0]
for i in range(n):
    for j in range(m):
        if A[i][j] < min:
            min = A[i][j]

print(min)



