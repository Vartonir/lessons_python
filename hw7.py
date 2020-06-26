"""
Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

only_profit = []
average_profit = {}
company_income = {}

with open("company.txt", "r+", encoding="UTF-8") as f_firm:
    for i in f_firm.read().split('\n'):
        i_split = i.split()
        profit = int(i_split[2]) - int(i_split[3])
        company_income[i_split[0]] = profit
        if profit > 0:
            only_profit.append(profit)
        average_profit["Средний доход фирм"] = int((sum(map(int, only_profit))) / (len(only_profit)))
json_list = [company_income, average_profit]
print(json_list)
with open("file_js.json", "w", encoding="UTF-8") as f_json:
    json.dump(json_list, f_json, ensure_ascii=False)
