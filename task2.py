num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'четных - {even}, нечетных - {odd}')
