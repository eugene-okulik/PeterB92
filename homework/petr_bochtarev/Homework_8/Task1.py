import random

while True:
    salary = int(input('Какая у вас зарплата ?'))
    bonus = random.choice([True, False])
    if bonus:
        print(f"• {salary}, {bonus} - '${salary + random.randint(1, 2000)}'")
    else:
        print(f"• {salary}, {bonus} - '${salary}'")
