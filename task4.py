x = int(input('Сколько элементов: '))
item = 1
x_sum = 0
for i in range(x):
    x_sum += item
    item /= -2
print(x_sum)
