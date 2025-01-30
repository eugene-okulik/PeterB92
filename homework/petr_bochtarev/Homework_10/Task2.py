# Эти задания пока что были самыми сложными, сначала было прям тяжко. Пересмотрел урок раза 3-4
# Основную часть второго задания почти полностью сделал сам, понял, что нужен цикл, но вот 8 строку пришлось
# подсмотреть через чат gpt, не понимал как можно реализовать count.


def repeat(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for x in range(count):
            func(*args, **kwargs)
    return wrapper


@repeat
def example(text):
    print(text)


example('print me', count=5)
print('========================================================')
# Далее идет дополнительная часть второго задания. Сначала пробовал без чата gpt. Нашел в гугле, что для использования
# параметра в декораторе, необходимо весь декоратор обернуть ещё в одну функцию и там использовать параметр.
# Далее попробовал через цикл вывести несколько раз результат работы, как делалось выше. Но не получилось
# Продолжение ниже

# НЕКОРРЕКТНАЯ РЕАЛИЗАЦИЯ


def decorator(count):
    for x in range(count):
        def repeat_func(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result
            return wrapper
        return repeat_func


@decorator(count=3)
def example(text):
    print(text)


example('print me')
print('========================================================')
# Снова обратился к чату gpt, чтобы понять, что не так. В итоге стало понятно(надеюсь, правильно понимаю теперь),
# что все действия надо производить внутри wrapper.
# Буду ещё пересматривать урок, чтобы всё закрепить.


def repeat_me(count):
    def decorator_test(func):
        def wrapper(*args, **kwargs):
            for x in range(count):
                result = func(*args, **kwargs)
        return wrapper
    return decorator_test


@repeat_me(count=3)
def example(text):
    print(text)


example('print me')
