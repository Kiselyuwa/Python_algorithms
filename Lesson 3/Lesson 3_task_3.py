# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# специально поломала размер матрицы (size+4), чтобы проверить.

import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
m = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE + 4)]
print(*m, sep='\n')

mc = []
for j in range(len(m[0])):
    min_el = m[0][j]
    for i in range(1, len(m) - 1):
        if min_el > m[i][j] < m[i + 1][j]:
            min_el = m[i][j]
    if min_el > m[len(m) - 1][j]:
        min_el = m[len(m) - 1][j]
    mc.append(min_el)

print(f'\n{mc} - список минимальных элементов столбцов матрицы')

max_mc = mc[0]
for el in mc:
    if el > max_mc:
        max_mc = el

print(f'\n{max_mc} - максимальный элемент среди минимальных элементов столбцов матрицы')
