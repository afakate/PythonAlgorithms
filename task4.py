"""Определить, какое число в массиве встречается чаще всего"""

import random

SIZE = 20
MIN_ITEM = 10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

num = array[0]
counter = 1
for i in range(len(array)):
    temp = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            temp += 1
    if temp > counter:
        counter = temp
        num = array[i]

print(f'Число {num} встречается {counter} раз(а)' if counter > 1 else 'Все числа встречаются только один раз')
