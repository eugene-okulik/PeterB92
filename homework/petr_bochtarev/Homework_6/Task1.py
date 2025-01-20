text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, ' \
       'dignissim vitae libero'
words = text.split()
modified_text = []
for value in words:
    if ',' in value or '.' in value:
        value = f'{value[:-1]}ing{value[-1]}'
        modified_text.append(value)
    else:
        value = f'{value}ing'
        modified_text.append(value)
print(' '.join(modified_text))
