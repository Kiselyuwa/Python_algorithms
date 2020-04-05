#
# https://drive.google.com/file/d/1Keu-r7_bMuRP1eSlIfqMeXiO6SMjtKMZ/view?usp=sharing
# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Ведите число а: '))
b = float(input('Ведите число b: '))
c = float(input('Ведите число c: '))

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число b = {b}')
        else:
            print(f'Среднее число c = {c}')
    else:
        print(f'Среднее число a = {a}')
elif b > c:
    if a > c:
        print(f'Среднее число a = {a}')
    else:
        print(f'Среднее число c = {c}')
else:
    print(f'Среднее число b = {b}')
