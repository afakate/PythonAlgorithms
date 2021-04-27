"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква"""

# https://drive.google.com/file/d/17yG1Am9FFFGKFjzz0tzz-3KDwhHHglEA/view?usp=sharing

x = int(input('Номер буквы в алфавите: '))
x = ord('a') + x - 1
print(f'Буква: {chr(x)}')
