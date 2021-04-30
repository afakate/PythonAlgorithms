CONST = 10

num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * CONST + num % CONST
    num = num // CONST
print(result)
