"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""
name_lection = []
hours_lection = []
dict_lection = {}

with open("lection.txt", "r", encoding="UTF-8") as f_lection:
    for lection in f_lection:
        lection_spilt = lection.split(':')
        name_lection.append(lection_spilt[0])
        hours_lection.append(sum(map(int, "".join([i for i in lection if i == ' ' or ('0' <= i <= '9')]).split())))
    for i in range(len(name_lection)):
        dict_lection[name_lection[i]] = hours_lection[i]
    print(dict_lection)



