"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

average_salary = []
result = {}
with open("Salary.txt", "r", encoding="utf-8") as f_obj:
    for i in f_obj.read().split("\n"):
        i = i.split(":")
        result[i[0]] = i[1]
    for key, value in result.items():
        if int(value) < 20000:
            print(f"{key} получает {value}, а это меньше 20000")
        average_salary.append(value)
    print(f"Средняя зарплата сотрудников {(sum(map(int,average_salary)))/(len(average_salary))} тугриков")
