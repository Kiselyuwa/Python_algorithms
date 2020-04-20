# 2.2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from collections import defaultdict

dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


# находим сумму
def summa_16(a, b):
    summa = deque()
    rest = 0
    a.reverse()
    b.reverse()

    while len(a) != len(b):
        if len(a) < len(b):
            a.append('0')
        else:
            b.append('0')

    for i in range(len(a)):
        s = dict.get(a[i]) + dict.get(b[i]) + rest
        if s <= 15:
            summa.append((list(dict.keys()))[s])
            rest = 0
        else:
            summa.append((list(dict.keys()))[s - 16])
            rest = 1  # как при решении столбиком = "один в уме"
    summa.reverse()
    return summa


# находим произведение. Ответ: [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]. Смогла сделать только для того случая,
# когда хотя бы одно из чисел двузнаковое, то есть придется суммировать только 2 числа.
# И то кажется, что вышло громоздко

# a = deque(['A', '2'])
# b = deque(['C', '4', 'F'])
a = input('Введите первое шестнадцатиричное число: ')
b = input('Введите второе шестнадцатиричное число: ')

a = deque(list(a))
b = deque(list(b))

def mult_16(a, b):
    if len(a) > len(b):
        a, b = b, a

    a.reverse()
    b.reverse()
    mult = {key: [] for key in range(len(a) - 1)}
    mult = defaultdict(list)

    for i in range(len(a)):
        rest = 0
        if i > 0:
            mult[i].append('0')

        for j in range(len(b)):
            m = dict.get(a[i]) * dict.get(b[j]) + rest
            if m <= 15:
                mult[i].append(list(dict.keys())[m])
                rest = 0
            else:
                mult[i].append(list(dict.keys())[m % 16])
                rest = m // 16
                if j == (len(b) - 1) and rest != 0:
                    mult[i].append(str(rest))

    c = deque(mult[0])
    d = deque(mult[1])
    c.reverse()
    d.reverse()

    return summa_16(c, d)


print(mult_16(a, b))
