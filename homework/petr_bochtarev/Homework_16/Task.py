import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()
db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)
cursor = db.cursor()

all_info = '''
SELECT s.name, s.second_name, g.title, b.title, s2.title Предмет, l.title, m.value
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN `groups` as g  ON g.id = s.group_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjets s2 on l.subject_id = s2.id
JOIN books b ON s.id = b.taken_by_student_id
'''
cursor.execute(all_info)
data = (cursor.fetchall())
list_from_bd = list(map(list, data))
print(list_from_bd)
print('=' * 80)
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw16_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

list_from_file = []
with open(hw16_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    for row in file_data:
        list_from_file.append(row)
print(list_from_file)
print('=' * 80)

for element_file in list_from_file:
    if element_file == list_from_file[0]:
        continue
    else:
        need_to_print = True
        for element_bd in list_from_bd:
            if element_file == element_bd:
                need_to_print = False
                break
        if need_to_print:
            print(element_file)
