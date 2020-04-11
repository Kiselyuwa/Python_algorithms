# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

SIZE = 20
MIN_ITEM = -50
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_1 = min_2 = array[0]

for i in range(1, len(array)):
    if array[i] < min_1:
        min_2 = min_1
        min_1 = array[i]
    elif array[i] < min_2:
        min_2 = array[i]

print(min_1)
print(min_2)

# Вариант № 2, c использованием count
#
# min_1 = min_2 = array[0]
#
# for el in array:
#     if el < min_1:
#         min_1 = el
#     if array.count(min_1) > 1:
#         min_2 = min_1
#         break
#     elif min_1 < el < min_2:
#         min_2 = el
#
# print(min_1)
# print(min_2)



