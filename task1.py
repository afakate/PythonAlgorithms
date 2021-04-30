# https://drive.google.com/file/d/1hXGVgK-m9StJ2yRGggPNnFQlf3QFcQAZ/view?usp=sharing

def calc():
    sign = input('Знак: ')
    if sign == '0':
        return
    if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        x = float(input('x = '))
        y = float(input('y = '))
        if sign == '+':
            print(f'{x + y:.2f}')
        elif sign == '-':
            print(f'{x - y:.2f}')
        elif sign == '*':
            print(f'{x * y:.2f}')
        elif sign == '/':
            print(f'{x / y:.2f}')
        else:
            print('Делить на ноль нельзя')
    else:
        print('Неверный знак')
    return calc()


calc()
