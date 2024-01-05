#T23_11_v1
# Створення робочої книги MS Excel
# Зображення графіку функції f на інтервалі [a,b] у n точках

from openpyxl import *
from openpyxl.chart import (
    ScatterChart,
    LineChart,
    Reference,
    Series,
)

from T20.t20_11_tabulate_v3 import *
from math import sin


def plotfunc1(a, b, n, f):
    '''Зображує графік функції f на інтервалі [a,b] у n точках
    '''
    x, y = tabulate(f, a, b, n) # табулювати функцію
    wb = Workbook()             # створити робочу книгу 
    ws = wb.active              # вибрати активний робочий аркуш
    ws.append(['x', f.__name__])# додати заголовки стовпчиків
    for i in range(n):
        ws.append([x[i], y[i]]) # додати дані

    # побудуувати графік
    chart1 = ScatterChart()
    chart1.legend = None
    xdata = Reference(ws, min_col=1, min_row=2, max_row=n+1)
    ydata = Reference(ws, min_col=2, min_row=2, max_row=n+1)
    s = Series(ydata, xvalues=xdata)
    chart1.append(s)
    ws.add_chart(chart1, "E1")
    
    wb.save(f.__name__ + '.xlsx')   #зберегти робочу книгу

if __name__ == '__main__':
    n = int(input('Кількість точок: '))
    a = float(input('Початок відрізку: '))
    b = float(input('Кінець відрізку: '))


    funcs = [fun, sin]
    for ff in funcs:
        plotfunc1(a, b, n, ff)
