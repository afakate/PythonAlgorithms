"""Определить, является ли год, который ввел пользователем, високосным или невисокосным"""

# # https://drive.google.com/file/d/17yG1Am9FFFGKFjzz0tzz-3KDwhHHglEA/view?usp=sharing

year = int(input('Введите год: '))

if year % 4 != 0:
    print('Невисокосный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Високосный')
    else:
        print('Невисокосный')
else:
    print('Високосный')
