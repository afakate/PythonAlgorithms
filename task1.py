"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь"""

# https://drive.google.com/file/d/17yG1Am9FFFGKFjzz0tzz-3KDwhHHglEA/view?usp=sharing

x = int(input('Введите трехзначное число: '))
a = x // 100
b = x % 100 // 10
c = x % 10

dig_sum = a + b + c
dig_mult = a * b * c

print(f'Сумма = {dig_sum}')
print(f'Произведение = {dig_mult}')
