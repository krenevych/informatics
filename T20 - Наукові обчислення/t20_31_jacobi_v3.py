#T20_31_v3
#Розв'язання системи лінійних алгебраїчних рівнянь методом Якобі
#Перевірка сходимості ітерації. Введення системи з текстового файлу.
#Векторизація

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
    d = np.diag(a)          #діагональні елементи a
    dd = np.abs(d)*2        #подвоєні модулі діагональних елементів a
    na = np.sum(np.abs(a), axis = 1)  #суми модулів елементів рядків матриці a
    return np.all(dd >= na) and np.any(dd > na)

def jacobi(a, b, eps=1.0e-10):
    '''Розв'язує систему рівнянь ax=b методом Якобі.

    Використовує векторизацію
    '''
    if not check_convergence(a):
        raise ValueError("Не сходиться ітераційний процес")
    c = a.copy()
    d = np.diag(a)          #діагональні елементи a
    np.fill_diagonal(c, 0.0)#заповнюємо діагональні елементи c нулями
    c /= d[:,np.newaxis]    #ділимо всі елементи c на діагональні елементи a
    #ділення повинно відбуватись по рядках, а саме кожен елемент i-го рядку
    #матриці c треба ділити на i-й елемент d
    #для правильного поширення треба вектор d розглядати як вектор-стовпчик
    #або матрицю з 1 стовпчиком, що робиться за допомогою d[:,np.newaxis]
    g = b / d               #ділимо всі елементи b на діагональні елементи a
    
    x = g.copy()            #початкове наближення
    for it_count in range(ITERATION_LIMIT):
        print("Current solution:", x)
        x_new = g - np.dot(c, x) #обчислюємо нове наближення
        if np.sum(np.abs(x-x_new)) < eps: #перевірка на "близькість" x, x_new
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
print("Нев'язка:")
print(error)

#Розв'язання за допомогою linalg.solve
x_solve = np.linalg.solve(a,b)
print('linalg.solve')
print(x_solve)

solve_error = np.dot(a, x_solve) - b
print("Нев'язка linalg.solve:")
print(solve_error)


