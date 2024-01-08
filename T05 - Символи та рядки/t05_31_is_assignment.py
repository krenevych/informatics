# t05_31_is_assignment.py
# Перевірити, чи є рядок командою присвоєння у Python вигляду
# <змінна> = <ціле_число>

s=input('рядок: ')

eq_pos = s.find('=')

if eq_pos < 0:
    success = False     # результат перевірки
else:
    name = s[:eq_pos].strip()           # ім'я змінної
    number = s[eq_pos + 1:].strip()     # число
    if not name.isidentifier() or len(number) == 0:
        success = False
    else:
        sign = number[0]
        number2 = number[1:]
        success = sign in '+-' and number2.isdigit() or number.isdigit()

print("Те, що рядок є командою присвоєння - ", success)
