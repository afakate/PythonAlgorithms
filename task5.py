"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве"""

import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

print(array)

index = -1
for i in range(len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]}. Позиция в массиве {index}')