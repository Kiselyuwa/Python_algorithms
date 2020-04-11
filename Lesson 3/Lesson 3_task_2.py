# 4. Определить, какое число в массиве встречается чаще всего.
# Вариант № 1. Замучалась с подсчетом индексов, исполнение медленное.
# но получилось без count и set (с ними варианты ниже)

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 0
max_el = [0][0]
for i in range(SIZE - 1):
    count = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            count += 1
        if count > max_count:
            max_count = count
            max_el = array[i]

if max_count > 1:
    print(f'Число {max_el} встречается чаще всего: {max_count} раз(а)')
else:
    print(f'Все элементы встречаются ровно по одному разу')

# Вариант № 2. c использованием set. быстро работает,особенно, когда большой список, небольшой разброс значений.
# Но наверное set нельзя было использовать в Дз.. поэтому как вариант.
# import random
#
# SIZE = 1_000_000
# MIN_ITEM = 0
# MAX_ITEM = 10
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)
#
# unique_array = set(array)
# print(unique_array)
#
# max_count = 0
#
# for el in unique_array:
#     spam_count = array.count(el)
#     if spam_count > max_count:
#         max_count = spam_count
#         max_el = el
#
# if max_count > 1:
#     print(f'Число {max_el} в массиве встречается чаще всего: {max_count} раз(а)')
# else:
#     print(f'Все элементы в массиве встречаются ровно по одному разу')
#


# Вариант № 3. c использованием count, тоже медленно исполняется.
# import random
#
# SIZE = 10
# MIN_ITEM = 0
# MAX_ITEM = 5
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

# max_count = 0
# for el in array:
#     spam_count = array.count(el)
#     if spam_count > max_count:
#         max_count = spam_count
#         max_el = el

# if max_count > 1:
#     print(f'Число {max_el} в массиве встречается чаще всего: {max_count} раз(а)')
# else:
#     print(f'Все элементы в массиве встречаются ровно по одному разу')
