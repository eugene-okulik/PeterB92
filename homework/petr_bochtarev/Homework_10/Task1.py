def decorator_finish(func):
    def wrapper(*args):
        func(*args)
        print('finished')
    return wrapper


@decorator_finish
def greetings(name):
    print(f'Здравствуйте, {name}!')


greetings('Евгений')
