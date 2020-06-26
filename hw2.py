"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
count_string = 0
with open("counter_file.txt", encoding='utf-8') as f_obj:
    for n, i in enumerate(f_obj.readlines()):
        print(f"В строке {n + 1} содержится {len(i.split())} слов")
        count_string += 1
    print(f"Всего строк {count_string}")
