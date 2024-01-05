Lst = []
for i in range (10):
    Lst.append(i)
print(Lst)
try:
    n = int(input("Enter n:"))
    print(Lst[n])
except IndexError:
    print("Вихід за межі массиву. Виведено останній елемент:", Lst[len(Lst)-1])
