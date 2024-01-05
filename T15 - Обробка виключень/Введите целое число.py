x = True

while x == True:
    try:
        n = int(input("Enter n:"))

    except ValueError:
        print("Введите целое число")
    else:
        x = False
print("n = %d" %n)
