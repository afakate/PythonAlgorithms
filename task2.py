"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа"""

import random

SIZE = 10
MIN_ITEM = 10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

result = []
for index, item in enumerate(array):
    if item % 2 == 0:
        result.append(index)
print(f'Индексы четных элементов: {result}')
