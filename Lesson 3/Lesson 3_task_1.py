# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_1 = [el for el in range(2, 100)]
list_2 = [item for item in range(2, 10)]

for item in list_2:
    i = 0
    for el in list_1:
        if el % item == 0:
            i += 1
    print(f'{item} - {i}')
