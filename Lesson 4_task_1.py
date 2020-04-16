# Задача: Определить, какое число в массиве встречается чаще всего.
# да, можно было и без вывода самого массива, но иначе было бы непонятно работает код или нет, поэтому оставила в функции
# и формирование и вывод массива. По быстродействию 1 вариант наилучший. По проверке cProfile.run существенные различия
# есть только во времени подсчета count.

# Вариант № 1. Быстрый. Выбираю его) Единственный, которой не завис на значениях больше 2000 (10_000).
# Имеет линейную сложность.

import timeit
import cProfile
import random

def max_count(size):

    min_item = 0
    max_item = 10
    array = [random.randint(min_item, max_item) for _ in range(size)]

    unique_array = set(array)

    max_count = 1
    max_el = array[0]
    for el in unique_array:
        spam_count = array.count(el)
        if spam_count > max_count:
            max_count = spam_count
            max_el = el
    return array, max_el, max_count

array, max_el, max_count = max_count(10)
print(f'В массиве: {array}\nЧисло {max_el} встречается чаще всего: {max_count} раз(а)\n')
#
# print(timeit.timeit('max_count(10)', number=100, globals=globals()))  # 0.0011345
# print(timeit.timeit('max_count(50)', number=100, globals=globals()))  # 0.009351600000000002
# print(timeit.timeit('max_count(100)', number=100, globals=globals()))  # 0.0159898
# print(timeit.timeit('max_count(200)', number=100, globals=globals()))  # 0.0221974
# print(timeit.timeit('max_count(300)', number=100, globals=globals()))  # 0.032012
# print(timeit.timeit('max_count(400)', number=100, globals=globals()))  # 0.04229219999999999
# print(timeit.timeit('max_count(500)', number=100, globals=globals()))  # 0.06045299999999998
# print(timeit.timeit('max_count(1_000)', number=100, globals=globals()))  # 0.1231836
# print(timeit.timeit('max_count(2_000)', number=100, globals=globals()))  # 0.21326399999999998
# print(timeit.timeit('max_count(10_000)', number=100, globals=globals()))  # 1.035815

# cProfile.run('max_count(10)')  #   1    0.000    0.000    0.000    0.000 Lesson 4_task_1.py:7(max_count)
# cProfile.run('max_count(100)')  #  1    0.000    0.000    0.000    0.000 Lesson 4_task_1.py:7(max_count)
# cProfile.run('max_count(1_000)')  #  1    0.000    0.000    0.002    0.002 Lesson 4_task_1.py:7(max_count)
# cProfile.run('max_count(2_000)')  #  1    0.000    0.000    0.003    0.003 Lesson 4_task_1.py:7(max_count)
# cProfile.run('max_count(10_000)') #  1    0.000    0.000    0.016    0.016 Lesson 4_task_1.py:7(max_count)


#  Вариант № 2. хуже 1ого варианта, но лучше 3его, середина.
# У функции нет 2х вложенных циклов, но при одинаковом изменении объема данных, время растет все больше и больше.
# Похоже на квадратичную функцию.

def max_count(size):

    min_item = 0
    max_item = 10
    array = [random.randint(min_item, max_item) for _ in range(size)]

    max_el = array[0]
    max_count = 1
    for el in array:
        spam_count = array.count(el)
        if spam_count > max_count:
            max_count = spam_count
            max_el = el
    return array, max_el, max_count

array, max_el, max_count = max_count(10)
print(f'В массиве: {array}\nЧисло {max_el} встречается чаще всего: {max_count} раз(а)\n')


# print(timeit.timeit('max_count(10)', number=100, globals=globals()))  # 0.0011806999999999998
# print(timeit.timeit('max_count(50)', number=100, globals=globals()))  # 0.0077408000000000025
# print(timeit.timeit('max_count(100)', number=100, globals=globals()))  # 0.021244300000000004
# print(timeit.timeit('max_count(200)', number=100, globals=globals()))  # 0.0676927
# print(timeit.timeit('max_count(300)', number=100, globals=globals()))  # 0.13841179999999997
# print(timeit.timeit('max_count(400)', number=100, globals=globals()))  # 0.24898729999999997
# print(timeit.timeit('max_count(500)', number=100, globals=globals()))  # 0.35881470000000004
# print(timeit.timeit('max_count(1_000)', number=100, globals=globals()))  # 1.3979576
# print(timeit.timeit('max_count(2_000)', number=100, globals=globals()))  # 5.2170816

# cProfile.run('max_count(10)')  #   1    0.000    0.000    0.000    0.000 Lesson 4_task_1.py:75(max_count)
# cProfile.run('max_count(100)')  #  1    0.000    0.000    0.000    0.000 Lesson 4_task_1.py:75(max_count)
# cProfile.run('max_count(1_000)')  #  1    0.000    0.000    0.015    0.015 Lesson 4_task_1.py:75(max_count)
# cProfile.run('max_count(2_000)')  #  1  0.000    0.000    0.054    0.054 Lesson 4_task_1.py:75(max_count)


# Вариант № 3 . Самый медленный. Имеет 2 вложенных цикла, значит имеет квадратичную сложность.

def max_count(size):

    min_item = 0
    max_item = 10
    array = [random.randint(min_item, max_item) for _ in range(size)]

    max_count = 1
    max_el = array[0]
    for i in range(len(array) - 1):
        count = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
            if count > max_count:
                max_count = count
                max_el = array[i]
    return array, max_el, max_count

array, max_el, max_count = max_count(10)
print(f'В массиве: {array}\nЧисло {max_el} встречается чаще всего: {max_count} раз(а)\n')


# print(timeit.timeit('max_count(10)', number=100, globals=globals()))  # 0.001501800000000001
# print(timeit.timeit('max_count(50)', number=100, globals=globals()))  # 0.015136500000000004
# print(timeit.timeit('max_count(100)', number=100, globals=globals()))  # 0.0446046
# print(timeit.timeit('max_count(200)', number=100, globals=globals()))  # 0.152719
# print(timeit.timeit('max_count(300)', number=100, globals=globals()))  # 0.40340529999999997
# print(timeit.timeit('max_count(400)', number=100, globals=globals()))  # 0.6015653000000001
# print(timeit.timeit('max_count(500)', number=100, globals=globals()))  # 0.9396093000000001
# print(timeit.timeit('max_count(1_000)', number=100, globals=globals()))  # 3.7031657
# print(timeit.timeit('max_count(2_000)', number=100, globals=globals()))  # 14.340697499999997

# cProfile.run('max_count(10)')  #  1    0.000    0.000    0.000    0.000 Lesson 4_task_1.py:9(max_count)
# cProfile.run('max_count(100)')  #  1    0.000    0.000    0.001    0.001 Lesson 4_task_1.py:9(max_count)
# cProfile.run('max_count(1_000)') #  1    0.041    0.041    0.043    0.043 Lesson 4_task_1.py:9(max_count)
# cProfile.run('max_count(2_000)') #  1    0.139    0.139    0.142    0.142 Lesson 4_task_1.py:9(max_count)
