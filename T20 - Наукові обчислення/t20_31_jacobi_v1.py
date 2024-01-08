#T20_31_v1
#Розв'язання системи лінійних алгебраїчних рівнянь методом Якобі
#Програму взято з https://en.wikipedia.org/wiki/Jacobi_method

import numpy as np

ITERATION_LIMIT = 1000

# initialize the matrix
a = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

# prints the system
print("System:")
for i in range(a.shape[0]):
#a.shape[0] - кількість рядків, a.shape[1] - кількість стовпчиків матриці    
    row = ["{}*x{}".format(a[i, j], j + 1) for j in range(a.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b) #масив нулів такого ж розміру, як b
for it_count in range(ITERATION_LIMIT):
    print("Current solution:", x)
    x_new = np.zeros_like(x) #масив нулів такого ж розміру, як x

    for i in range(a.shape[0]):
        s1 = np.dot(a[i, :i], x[:i])            #добуток до i компоненти
        s2 = np.dot(a[i, i + 1:], x[i + 1:])    #добуток після i компоненти
        x_new[i] = (b[i] - s1 - s2) / a[i, i]

    if np.allclose(x, x_new, atol=1e-15): #перевірка на "близькість" x, x_new
        break

    x = x_new

print("Solution:")
print(x)
error = np.dot(a, x) - b
print("Error:")
print(error)
