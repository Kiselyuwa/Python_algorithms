# https://drive.google.com/file/d/1cIzjEAsyOOx76SPt2LsB_GOcc-vBFRU6/view?usp=sharing
# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Введите натуральное число: '))

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f'В веденном числе четных цифр : {even}, нечетных: {odd}')
