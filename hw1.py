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