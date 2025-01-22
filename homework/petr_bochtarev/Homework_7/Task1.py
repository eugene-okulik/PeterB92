secret_number = 5
print('Попробуйте угадать цифру, которую мы загадали')
while True:
    user_number = int(input('Введите цифру:'))
    if secret_number == user_number:
        print('“Поздравляю! Вы угадали!”')
        break
    else:
        print('Вы не угадали, попробуйте снова')

# secret_number = 40
# print('Попробуйте угадать число от 1 до 100, которое мы загадали')
# number_of_attempts = 0
# prom = 0
# while True:
#     user_number = int(input('Введите число:'))
#     if secret_number == user_number:
#         print('“Поздравляю! Вы угадали!”')
#         number_of_attempts += 1
#         break
#     else:
#         if number_of_attempts != 0:
#             if user_number > secret_number + 30:
#                 if user_number >= prom > 0:
#                     print('Надо же было число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#                 else:
#                     print('Слишком большое число, попробуй число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#             elif user_number > secret_number + 20:
#                 if user_number >= prom > 0:
#                     print('Надо же было число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#                 else:
#                     print('Большое число, попробуй число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#             elif user_number > secret_number + 5:
#                 if user_number >= prom > 0:
#                     print('Надо же было число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#                 else:
#                     print('Уже ближе, попробуй число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#             elif user_number > secret_number:
#                 if user_number >= prom > 0:
#                     print('Надо же было число поменьше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#                 else:
#                     print('Очень близко, попробуй число немного меньше')
#                     number_of_attempts += 1
#                     prom = user_number
#                     continue
#             elif user_number < secret_number:
#                 print('Маленькое число, попробуй число побольше')
#                 number_of_attempts += 1
#                 prom = user_number
#                 continue
#         print('Вы не угадали, попробуйте снова. C первого раза угадать очень трудно')
#         number_of_attempts += 1
# print(f'Количество попыток для отгадывания: {number_of_attempts}')
