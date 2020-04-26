#  3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
#  Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
#  медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import timeit
import cProfile
import random

m = 5
arr = [random.randint(1, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив {arr}')

print(f'Отсортированный массив для проверки {sorted(arr)}')


# Вариант 1. медианой будет число, которое имеет слева и справа от себя равное кол-во элементов.
def median_1(arr):
    for j in range(len(arr)):
        left = right = 0
        same = -1
        for i in range(len(arr)):
            if arr[j] > arr[i]:
                left += 1
            elif arr[j] < arr[i]:
                right += 1
            elif arr[j] == arr[i]:  # если есть много повторов одинакового числа, считаем
                same += 1
        # print(left, same, right)
        if left == right or same + left == right or same + right == left:
            return arr[j]


print(f'Медиана массива = {median_1(arr)}')


# Вариант 2. Не лучший по времени, но рабочий вариант.
# Находим max и min элементы в массиве и убираем их. Остается 1 число - медиана.
def max_min(arr):
    max_ = arr[0]
    min_ = arr[0]
    i = 1
    for j in range(i, len(arr)):
        if arr[i] > arr[j] and arr[i] > max_:
            max_ = arr[i]
        elif arr[j] < min_:
            min_ = arr[j]
        elif arr[j] > max_:
            max_ = arr[j]
        j += 1
    return max_, min_


def median_2(arr):
    while len(arr) != 1:
        arr.remove(max_min(arr)[0])
        arr.remove(max_min(arr)[1])
    return arr[0]


# print(max_min(arr))
print(f'Медиана массива = {median_2(arr)}')


# Вариант 3. То же самое, только с использованимем max, min.
def median_3(arr):
    while len(arr) != 1:
        arr.remove(max(arr))
        arr.remove(min(arr))
    return (arr[0])


print(f'Медиана массива = {median_3(arr)}')
