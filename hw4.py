"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

translate = ["Один", "Два", "Три", "Четыре"]
counter = 0

with open("russian-numbers.txt", "a", encoding="UTF-8") as file_rus:
    with open("english_numbers.txt", 'r', encoding="utf-8") as file_eng:
        for i in file_eng.read().split("\n"):
            i = i.split(" - ")
            file_rus.writelines(translate[counter] + ' - ' + i[1] + "\n")
            counter += 1



