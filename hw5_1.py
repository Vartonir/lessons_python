"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint
counters = 0

with open("numbers_1.txt", "r+", encoding="UTF-8") as f_numbers:
    for i in range(3):
        random_number = randint(1, 1000)
        counters += random_number
        f_numbers.writelines(str(random_number) + " ")
    print(f"Сумму чисел в файле: {counters}")
