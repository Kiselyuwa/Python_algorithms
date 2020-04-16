# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
# Пример работы программ:
#
# sieve(2)
# 3


import timeit
import cProfile


# функция нахождения чисел по алгоритму «Решето Эратосфена». Использую для словаря
def sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res


# формируем словарь. Ключ = индекс: значение = n (из какого объема формировать массив простых чисел)
def prime_dict(sieve):
    count = 0
    left = 0
    right = 100
    dict = {}
    for el in sieve:
        if left < el < right:
            dict.update({count: right})
        else:
            dict.update({count: right})
            left += 100
            right += 100
        count += 1
    return dict


# при частом использовании словарь можно прогрузить на большое кол-во элементов и вставить в код, не создавая каждый раз
prime_dict = prime_dict(sieve(1_000_000))


# 1). функция нахождения простого числа: принимает на вход натуральное и возвращает соответствующее простое число
# по алгоритму «Решето Эратосфена». Линейная сложность. Справляется с большими значениями быстро.
def _sieve(k):
    if k in prime_dict.keys():
        n = prime_dict.get(k)

    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    #  print(res)  #  для проверки - какой длины массив простых чисел распечатывается
    return res[k - 1]


print(_sieve(14))


# print(timeit.timeit('_sieve(10)', number=100, globals=globals()))  # 0.0017164999999999542
# print(timeit.timeit('_sieve(20)', number=100, globals=globals()))  # 0.0017228999999999717
# print(timeit.timeit('_sieve(30)', number=100, globals=globals()))  # 0.0037598999999999827
# print(timeit.timeit('_sieve(40)', number=100, globals=globals()))  # 0.0035257000000000205
# print(timeit.timeit('_sieve(50)', number=100, globals=globals()))  # 0.0056446
# print(timeit.timeit('_sieve(100)', number=100, globals=globals()))  # 0.012490699999999966
# print(timeit.timeit('_sieve(1000)', number=100, globals=globals()))  # 0.19737899999999997
# print(timeit.timeit('_sieve(10000)', number=100, globals=globals()))  # 2.9797326

# cProfile.run('_sieve(10)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(20)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(30)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(40)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(50)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(100)')  # 1    0.000    0.000    0.000    0.000 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(1000)')  # 1    0.002    0.002    0.002    0.002 Lesson 4_task_2.py:55(_sieve)
# cProfile.run('_sieve(10000)')  # 1    0.024    0.024    0.030    0.030 Lesson 4_task_2.py:55(_sieve)


# 2). Второй — без использования «Решета Эратосфена». Да, использую append, который тормозит все действо. Но без него,
# если использовать по аналогии с прошлым решением замена непростых чисел нулями - выйдет ошибка (на ноль делить
# нельзя) cProfile.run - чем больше запрашиваемое число - тем больше вызов метода - вставки простого числа в массив.
# квадратичная сложность. на значении 10000 - завис,не справился.


def prime(k):
    if k in prime_dict.keys():
        n = prime_dict.get(k)

    prime = []
    for i in range(2, n + 1):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime[k - 1]


print(prime(14))


# print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.0019948000000000188
# print(timeit.timeit('prime(20)', number=100, globals=globals()))  # 0.002032099999999981
# print(timeit.timeit('prime(30)', number=100, globals=globals()))  # 0.005469000000000002
# print(timeit.timeit('prime(40)', number=100, globals=globals()))  # 0.00547930000000002
# print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.009585100000000013
# print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.02661190000000002
# print(timeit.timeit('prime(1000)', number=100, globals=globals()))  # 2.2952655
# # print(timeit.timeit('prime(10000)', number=100, globals=globals()))  # завис


# cProfile.run('prime(10)')  # 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(20)')  # 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(30)')  # 46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(40)')  # 46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(50)')  # 62    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(100)')  # 109    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(1000)')  # 1007    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('prime(10000)')  # 10006    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}


#  информативная доп. функция - видно в каком промежутке n - какие индексы значений простых чисел.
# Нужна была как промежуточная ступень для понимания, как сформировать словарь.
def n_index_sieve(sieve):
    count = 0
    count_l = 0
    count_r = 0
    left = 0
    right = 100

    for el in sieve:
        if left < el < right:
            count += 1
        else:
            count_r = count_r + count
            print(f' от {left} до {right} n = индексы простого числа от {count_l} до {count_r}')
            count = 1
            count_l = count_r + 1
            left += 100
            right += 100


n_index_sieve((sieve(500)))
