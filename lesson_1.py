# Первое задание

a = 47
b = 'Первый шаг'
c = 15.951

print(a, type(a))
print(b, type(b))
print(c, type(c))

number_entry = int(input('Введите число: '))
text_entry = input('Введите текст: ')
dro_entry = float(input('Введите дробное число: '))

print(f'Ваше число {number_entry} ', type(number_entry))
print(f'Ваш текст: {text_entry} ', type(text_entry))
print(f'Ваше дробное число: {dro_entry} ', type(dro_entry))

# Второе задание

time_seconds_entry = int(input("Введите время в секундах: "))

time_hh = time_seconds_entry // 3600
time_mm = time_seconds_entry % 3600 // 60
time_ss = time_seconds_entry % 3600 % 60

print(f'Получилось {time_hh:02}:{time_mm:02}:{time_ss:02}')

# Третье задание

n = input('Введите число n: ')


print(f'Сумма {n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')

# Четвёртое задание

number_entry = int(input('Введите положительное число: '))

while number_entry < 0:
    number_entry = int(input('Введите только положительное число!! : '))

m = number_entry % 10   # максимальное число
b = number_entry // 10

while b > 0:
    if b % 10 > m:
        m = b % 10
    b = b // 10

print('Максимальное цифра из числа ', m)


# Пятое задание

prihod = int(input('Введите сумму выручки фирмы: '))
rashod = int(input('Введите расход фирмы: '))

if prihod > rashod:
    print('Прибыль — выручка больше издержек')
    pribyl = prihod - rashod
    s = pribyl/prihod
    print(f'Рентабельность выручки: {s}')
    people = int(input('введите число сотрудников: '))
    prihod_per_people = int(pribyl / people)
    print(f'Прибыль на одного сотрудника: {prihod_per_people}')
else:
    print('убыток — издержки больше выручки')

# Шестое задание

"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен 
увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который 
общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
"""


a = 15
b = 50
n = 0

while a < b:
    a = a + a*0.1
    n = n + 1

print(n)






