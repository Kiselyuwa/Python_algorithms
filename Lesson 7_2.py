#  2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
#  на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 10
arr = [round(random.random() * 50, 2) for _ in range(size)]  # .uniform(0, 50) подошел бы, если можно было бы включать правую границу
print(f'Исходный массив {arr}')


def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge_num(left, right)


def merge_num(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i == len(left):
        res.extend(right[j:])
    else:
        res.extend(left[i:])
    return res


print(f'Отсортированный массив {merge_sort(arr)}')
