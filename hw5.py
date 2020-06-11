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
