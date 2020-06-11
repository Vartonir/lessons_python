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