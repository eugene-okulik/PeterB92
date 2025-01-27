import datetime

data = 'Jan 15, 2023 - 12:05:33'
data_python = datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S')
only_month = data_python.strftime('%B')
data2 = data_python.strftime('%d.%m.%Y, %H:%M')
print(f'1. {only_month}')
print(f'2. {data2}')
