FIRST = 32
LAST = 127
STEP = 10

for i in range(FIRST, LAST + 1):
    print(f'\t{i}-{chr(i)}', end='')
    if i % STEP == FIRST % STEP - 1:
        print()
