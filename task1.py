"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9"""

START_RANGE = 2
END_RANGE = 99
FIRST_NUM = 2
LAST_NUM = 9

for i in range(FIRST_NUM, LAST_NUM + 1):
    counter = 0
    for j in range(START_RANGE, END_RANGE + 1):
        if j % i == 0:
            counter += 1
    print(f'Числу {i} кратно {counter} чисел')
