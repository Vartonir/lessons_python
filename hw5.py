"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers_list = []
print("Программа считает суму введеных чисел.")
with open("numbers.txt", "w", encoding="UTF-8") as f_numbers:
    while True:
        a = input("Введите число: ")
        print("Для выхода из программы нажмите Enter")
        if not a:
            break
        numbers_list.append(a)
    summa = sum(map(int,numbers_list))
    f_numbers.writelines(' '.join(numbers_list))
    print(f"Сумма чисел в файле {summa}")
