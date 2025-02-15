import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
cursor.execute("INSERT INTO students (name, second_name) VALUES ('Petr2', 'Bochtarev2')")
student_id = cursor.lastrowid
add_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    add_books, [
        ('Война и мир', student_id),
        ('Преступление и наказание', student_id),
    ]
)
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) "
    "VALUES ('Краснодар2', '2025-15-02 13:50:00.000000', '2025-15-02 14:00:00.000000')"
)
group_student_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (group_student_id, student_id))
cursor.execute("INSERT INTO subjets (title) VALUES ('Астрономия')")
subject1_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('Физика')")
subject2_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Пульсары', %s)", (subject1_id,))
lesson1_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Туманности', %s)", (subject2_id,))
lesson2_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Классическая механика', %s)", (subject1_id,))
lesson3_id = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES ('Релятивистская механика', %s)", (subject2_id,))
lesson4_id = cursor.lastrowid

add_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    add_marks, [
        (5, lesson1_id, student_id),
        (5, lesson2_id, student_id),
        (5, lesson3_id, student_id),
        (5, lesson4_id, student_id),
    ]
)
db.commit()
cursor.execute("SELECT value FROM marks WHERE student_id = 4318")
print(cursor.fetchall())
cursor.execute("SELECT title FROM books WHERE taken_by_student_id = 4318")
print(cursor.fetchall())
all_info = '''
SELECT s.name Имя, s.second_name Фамилия, g.title Группа, m.value Оценка_за_урок, l.title Название_занятия,
s2.title Предмет, b.title Книга
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN `groups` as g  ON g.id = s.group_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjets s2 on l.subject_id = s2.id
JOIN books b ON s.id = b.taken_by_student_id -- Из-за добавления книг, происходит дублирование строк
WHERE s.id = 4318;
'''
cursor.execute(all_info)
print(cursor.fetchall())
db.close()
