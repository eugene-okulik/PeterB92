one = 'результат операции: 42'
two = 'результат операции: 514'
three = 'результат работы программы: 9'
four = 'результат: 2'


def task(x):
    return int(x.split()[-1]) + 10


print(task(one))
print(task(two))
print(task(three))
print(task(four))
