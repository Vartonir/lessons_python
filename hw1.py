"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    text = input("Введите строку: ").split()
    if not text:
        break
    # print(text)
    with open("my_file.txt", "a+") as my_obj:
        for i in range(len(text)):
            print(text[i], file=my_obj)

