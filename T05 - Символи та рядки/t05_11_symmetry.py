#T05_11
#Перевірка рядка на симетричність

s=input("введіть рядок: ")

b=True                          #фіксує, чи є рядок симетричним
i=0                             #номер символа, який перевіряється
n=len(s)
while i < n//2 and b:
    b = s[i] == s[-(i+1)]       #перевіряемо, чи рівні символи, що рівновіддалені
                                #від початку та кінця рядка 
    i = i+1

if b:
    print (s,"- симетричний")
else:
    print (s,"- несиметричний")

