import statistics

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30,
    29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31,
    30, 32, 30, 28, 24, 23
]
hot_days_list = list(filter(lambda x: x > 28, temperatures))
print(hot_days_list)
print(f'Самая высокая температура: {max(hot_days_list)}')
print(f'Самая низкая температура: {min(hot_days_list)}')
print(f'Средняя температура: {round(statistics.mean(hot_days_list))}')
