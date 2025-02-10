import os
import chardet
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

# У меня русский текст из файла выводился разными символами, пришлось найти, как это обойти
with open(hw13_file_path, 'rb') as file:
    task_file = file.read()
    result = chardet.detect(task_file)
    encoding = result['encoding']
    print(f'Кодировка: {encoding}')

with open(hw13_file_path, encoding=encoding) as file:
    task_file = file.read()
    print(task_file)
print('=' * 70)
# Основная часть ДЗ
with open(hw13_file_path) as file:
    for line in file:
        data_python = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
        if line[0] == '1':
            print(f'1. {data_python + datetime.timedelta(days=7)}')
        elif line[0] == '2':
            print(f'2. {data_python.weekday()}')
        elif line[0] == '3':
            date3_changed = (datetime.datetime.now() - data_python)
            print(f'3. {date3_changed.days}')

# dates = []
# with open(hw13_file_path) as file:
#     for line in file:
#         date = line[3:29]
#         dates.append(date)
# print(dates)
# print('='*70)
#
#
# def date_python(index):
#     return datetime.datetime.strptime(dates[index], '%Y-%m-%d %H:%M:%S.%f')
#
#
# date1_python = date_python(0)
# date2_python = date_python(1)
# date3_python = date_python(2)
#
# print(date1_python + datetime.timedelta(days=7))
#
# date2_changed = date2_python.weekday()
# print(date2_changed)
#
# date3_changed = datetime.datetime.now() - date3_python
# print(date3_changed.days)
