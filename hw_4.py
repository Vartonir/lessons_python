"""

4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.

"""

while True:
    try:
        entry_x = int(input('Введите положительное число: '))
        while entry_x <= 0:
            entry_x = int(input('Введите положительное число, а не отрицательное: '))
        break
    except ValueError:
        print('Введите число ещё раз')

while True:
    try:
        entry_y = int(input('Введите отрицательное число: '))
        while entry_y >= 0:
            entry_y = int(input('Введите отрицательное число, а не положительное: '))
        break
    except ValueError:
        print('Введите число ещё раз')


def my_func(x, y):
    n_y = y * -1
    n_x = x
    while n_y > 1:
        n_x = n_x * x
        n_y -= 1
    return 1 / n_x


print(my_func(entry_x, entry_y))


