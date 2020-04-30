# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком. Пример работы функции:
# func("papa")
# 6      p a pa ap pap apa
# func("sova")
# 9      s o v a so ov va sov ova

import hashlib


def rabin_karp(s):
    hash = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            hash_sub = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            hash.add(hash_sub)  # одинаковый hash не будет добавляться в set
    # print(hash)
    return f'Количество различных подстрок в строке: \'{s}\'= {len(hash) - 1}'


s_1 = 'sova'
s_2 = 'papa'
s_3 = 's s'

print(rabin_karp(s_1))
print(rabin_karp(s_2))
print(rabin_karp(s_3))
