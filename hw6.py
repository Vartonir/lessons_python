"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools

"""
from itertools import cycle, count

b = 0
for el in count(10):
    if b > 10:
        break
    print(el)
    b += 1

name_list = list(input('Введите 3 любых имени через пробел').split())

repeat = cycle(name_list)

for n in count():
    if n > 10:
        break
    else:
        print(f"{n} - {next(repeat)}")
