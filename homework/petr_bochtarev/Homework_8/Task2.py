def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1


for number in fibonacci():
    if count in (5, 200, 1000, 100000):
        print(number)
        count += 1
    elif count < 100000:
        count += 1
    else:
        break
