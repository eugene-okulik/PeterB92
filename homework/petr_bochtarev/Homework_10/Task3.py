# Тут делал всё сам. Возможно что-то намудрил, но работает)
def decor(func):
    def wrapper(first, second, operation_sign='+'):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
    return wrapper


first_number = int(input('Введите первое число:'))
second_number = int(input('Введите второе число:'))


@decor
def calc(first, second, operation_sign='+'):
    if operation_sign == '+':
        return first + second
    elif operation_sign == '-':
        return first - second
    elif operation_sign == '*':
        return first * second
    elif operation_sign == '/':
        return round(first / second, 2)


print(calc(first_number, second_number, '/'))

# Это я для себя сделал, просто практиковался:
#
# first = int(input('Введите первое число:'))
# second = int(input('Введите второе число:'))
# operation = input('Какую операцию вы хотите произвести ? Введите одну из арифметических операций: +, -, /, *:')
#
#
# def calc(number_first, number_second, operation_sign):
#     while operation_sign != ('+', '-', '*', '/'):
#         if operation_sign == '+':
#             return first + second
#         elif operation_sign == '-':
#             return first - second
#         elif operation_sign == '*':
#             return first * second
#         elif operation_sign == '/':
#             return round(first / second, 2)
#         else:
#             print('Введите один из операторов: +, -, /, * ')
#             operation_sign = input(
#                 'Какую операцию вы хотите произвести ? Введите одну из арифметических операций: +, -, /, *:'
#             )
#             continue
#
#
# print(calc(first, second, operation))
