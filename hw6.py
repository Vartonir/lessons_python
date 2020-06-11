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

begin_result = int(input("Укажите сколько спортсмен пробежал в 1-й день: "))
end_result = int(input("Укажите сколько должен пробегать спортсмен: "))
n = 1  # дни пробежок

while True:
    if begin_result <= 0 or end_result <= 0:
        print("Спортсмен не может пробегать меньше нуля км!!! ")
        begin_result = int(input("Укажите сколько спортсмен пробежал в 1-й день: "))
        end_result = int(input("Укажите сколько должен пробегать спортсмен: "))
    else:
        while begin_result < end_result:
            begin_result = begin_result + begin_result * 0.1
            n += 1
            print(f'Спортсмен достиг результата на {n}-й день {begin_result:.3} км')
        break

print(f"Спортсмену, чтобы достичь результат потребуется {n} дней")
