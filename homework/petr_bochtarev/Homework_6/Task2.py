sequence = range(1, 101)
new_sequence = []
for value in sequence:
    if value % 3 == 0 and value % 5 == 0:
        new_sequence.append('FuzzBuzz')
    elif value % 5 == 0:
        new_sequence.append('Buzz')
    elif value % 3 == 0:
        new_sequence.append('Fuzz')
    else:
        new_sequence.append(str(value))
for value2 in new_sequence:
    if value2 == 'Fuzz' or value2 == 'Buzz':
        print(value2.lower())
    else:
        print(value2)
