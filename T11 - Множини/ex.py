
s = input('Введіть файний рядок ')

my_set = {x for x in s if '0' <= x <= '9'}

print (my_set)

print ('Рядок містить %d унікальних цифр' % len(my_set))
