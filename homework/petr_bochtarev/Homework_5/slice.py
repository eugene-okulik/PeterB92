# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2
one = 'результат операции: 42'
two = 'результат операции: 514'
three = 'результат работы программы: 9'
print((int(one[one.index('42'):])) + 10)
print((int(two[two.index('514'):])) + 10)
print((int(three[three.index('9'):])) + 10)

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
# Вариант 1
print('Students', ', '.join(students),'study these subjects:', ', '.join(subjects))
# Вариант 2
students1, students2, students3 = students
subjects1, subjects2, subjects3 = subjects
print(f'Students {students1}, {students2}, {students3} study these subjects: {subjects1}, {subjects2}, {subjects3}')
