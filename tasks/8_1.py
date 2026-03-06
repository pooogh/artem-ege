# import itertools
# itertools.product()

from itertools import product
product()

comdi = list(product('ABC', repeat=3))
print(comdi[10][1])
# [] - список (массив)
# () - кортеж
# for i in range(len(comdi) - 1, -1, -1):
#     if i % 2 == 0:
# 27 items -> 0-26 len(x) - 1
# 28 items -> 0-27 len(x) - 2
# 6 -> 0 1 2 3 4 5 len(x) - 2
# 5 -> 0 1 2 3 4    len(x) - 1
# ind = 0
for i in range(len(comdi) - 1, 0, -2):
    if comdi[i][0] != 'B' and comdi[i][2] != 'B' and comdi[i].count('A') >= 2:
        print(i + 1)
        break

