#  PyCharm Community Edition 2019.2.6,   Windows 10, 64-разрядная ОС
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,Количество элементов (n) вводится с клавиатуры.

# Все варианты замерялись на значении n = 5

# Функция show: Размер каждого элемента кладем в список, выводим информацию по каждому элементу. Добавила id, чтобы
# визуально проверить, что объекты различны.

import sys

size_list = []


def show(x):
    size_list.append(sys.getsizeof(x))
    print(f'type={type(x)}, id={id(x)} ,size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


# Функция show_all: Для прохождения всех элементов кода, вывод списка размеров (для проверки)
# и их суммы размеров занятой памяти.


def show_all(*args):
    for x in args:
        show(x)
    print(size_list)
    print(sum(size_list))


# 1 вариант кода. Список размеров элементов [24, 24, 28, 28]. Итого 104 Кб

n = int(input('Введите количество элементов: '))

a = 1
i = 1
s = 0

while i <= n:
    i += 1
    s += a
    a = -a / 2

print(f'Сумма элементов = {s}')

show_all(s, a, n, i)

# 2 вариант кода. При использовании иттерируемых объектов, таких как список, множество, кортеж, самым экономным выходит
# кортеж = [24, 24, 28, 88, 28, 24, 24, 24, 24] Итого 288 Кб. Такой вариант можно использовать, если элементы списка
# могут понадобиться в дальнейшем.

n = int(input('Введите количество элементов: '))

a_list = []
a = 1
for i in range(n):
    a_list.append(a)
    a /= -2

#  если оставить просто list, то Список размеров элементов = [24, 24, 28, 128, 28, 24, 24, 24, 24] Итого 328 Кб
# a_list = set(a_list)  # Список размеров элементов = [24, 24, 28, 736, 24, 28, 24, 24, 24] Итого 936 Кб

a_list = tuple(a_list)  # Список размеров элементов = [24, 24, 28, 88, 28, 24, 24, 24, 24] Итого 288 Кб.

s = sum(a_list)
print(f'Сумма элементов = {s}')

show_all(s, a, n, a_list)

# 3 вариант кода. Формулу взяла с ответов по Дз. Конечно самый экономичный вариант из всех, т.к. используются только
# 2 переменные. Список размеров элементов = [24, 28] Итого 52 Кб. НО такую формулу надо знать, а если не знаешь, то
# из всех вариантов кода - по соотношению "цена - качество" больше подходит 1ый вариант.

n = int(input('Введите количество элементов: '))

s = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
print(f'Сумма элементов = {s}')

show_all(s, n)
