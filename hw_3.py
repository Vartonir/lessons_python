"""
3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.

 """


def my_func(one, two, three):
    if one >= two & three:
        if two >= three:
            return one + two
        else:
            return one + three
    else:
        return two + three


print(f'Сумма наибольших чисел: {my_func(2, 3, 3)}')
