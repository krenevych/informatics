#T20_31_v2
#Розв'язання системи лінійних алгебраїчних рівнянь методом Якобі
#Перевірка сходимості ітерації. Введення системи з текстового файлу.

import numpy as np

ITERATION_LIMIT = 1000

def print_system(a, b):
    '''Виводить на екран систему рівнянь.
    '''
    print("Система:")
    for i in range(a.shape[0]):
    #a.shape[0] - кількість рядків, a.shape[1] - кількість стовпчиків матриці    
        row = ["{}*x{}".format(a[i, j], j + 1) for j in range(a.shape[1])]
        print(" + ".join(row), " = ", b[i])
    print()

def check_convergence(a):
    '''Перевіряє, чи сходиться ітераційний процес для системи рівнянь з матрицею a.
    '''
    t = True
    k = 0
    for i in range(a.shape[0]):
        s = sum(abs(a[i,j]) for j in range(a.shape[1]) if i != j)
        if abs(a[i,i]) < s:
            t = False
            break
        k = k + int(abs(a[i,i]) > s)
    return t and k > 0

def jacobi(a, b):
    '''Розв'язує систему рівнянь ax=b методом Якобі.
    '''
    if not check_convergence(a):
        raise ValueError("Не сходиться ітераційний процес")
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
    return x

filename = input("Ім'я файлу: ")
ab = np.loadtxt(filename)
a = ab[:,:-1]   #усі елементи окрім останнього стовпчика
b = ab[:,-1]    #останній стовпчик
print_system(a, b)

x = jacobi(a, b)
print("Розі'язок:")
print(x)
error = np.dot(a, x) - b
print("Похибка:")
print(error)
