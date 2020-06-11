time_seconds_entry = int(input("Введите время в секундах: "))

time_hh = time_seconds_entry // 3600
time_mm = time_seconds_entry % 3600 // 60
time_ss = time_seconds_entry % 3600 % 60

print(f'Получилось {time_hh:02}:{time_mm:02}:{time_ss:02}')