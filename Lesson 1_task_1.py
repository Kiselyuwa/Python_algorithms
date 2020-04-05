#
# https://drive.google.com/file/d/1Keu-r7_bMuRP1eSlIfqMeXiO6SMjtKMZ/view?usp=sharing
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input("Введите трехзначное число: "))
a = x // 100
b = x // 10 % 10
c = x % 10
s = a + b + c
m = a * b * c
print(f'Сумма чисел = {s} ; произведение чисел = {m}')
