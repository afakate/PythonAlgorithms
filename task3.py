"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы"""

import random

SIZE = 10
MIN_ITEM = 10
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

i_min = 0
i_max = 0
for i in range(len(array)):
    if array[i] < array[i_min]:
        i_min = i
    elif array[i] > array[i_max]:
        i_max = i

array[i_min], array[i_max] = array[i_max], array[i_min]
print(array)
