import argparse
import os
from string import punctuation

parser = argparse.ArgumentParser()
parser.add_argument('directory', help='Путь до папки с файлами')
parser.add_argument('--text', help='Текст, который необходимо найти (указывается в кавычках)')
args = parser.parse_args()


def read_all_files_in_directory(files_path):
    for file_name in os.listdir(files_path):
        file_path = os.path.join(files_path, file_name)
        with open(file_path, encoding='utf-8') as file:
            for number_line, line in enumerate(file, start=1):
                yield line.strip(), file_name, number_line


punctuation_to_remove = punctuation.replace('_', '')
for line_file, name_file, line_number in read_all_files_in_directory(args.directory):
    string_without_punctuation = (
        line_file.translate(str.maketrans('', '', punctuation_to_remove))  # Удаляю все знаки пунктуации кроме '_'
    )
    words = string_without_punctuation.split()
    if args.text in words:
        index_args_text = words.index(args.text)
        start_index = max(0, index_args_text - 5)
        end_index = index_args_text + 6
        five_words_before_five_words_after = (
            words[start_index:index_args_text] + [f'*{args.text.upper()}*'] + words[(index_args_text + 1):end_index]
        )
        print('*' * 100)
        print(f'Название файла, в котором найдено совпадение: {name_file}')
        print(f'Строка файла, в которой найдено совпадение: {line_file}')
        print(f'Номер строки, в которой найдено совпадение: {line_number}')
        print('Пять слов ДО, пять слов ПОСЛЕ + слово из поиска: ', ' '.join(five_words_before_five_words_after))
        print('*' * 100)
        break
