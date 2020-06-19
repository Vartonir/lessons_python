"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Делеить на ноль нельзя'


while True:
    try:
        entry_1 = int(input('Введите первое число: '))
        entry_2 = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Введите число ещё раз')

print(my_func(entry_1, entry_2))
