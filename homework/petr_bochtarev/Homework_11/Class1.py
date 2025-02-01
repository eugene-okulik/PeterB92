class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_pages, isbn, reserve):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserve = reserve


book1 = Book('Война и мир', 'Лев Толстой', 2144, 9780393096729, True)
book2 = Book('Гамлет', 'Уильям Шекспир', 384, 978538902142, False)
book3 = Book('Одиссея', 'Гомер', 312, 9780312866693, False)
book4 = Book('Дон Кихот', 'Мигель де Сервантес', 1026, 9781853260360, False)
book5 = Book('Преступление и наказание', 'Фёдор Достоевский', 553, 780198709701, False)


def book_information(book):
    if book.reserve:
        print(
            f'Название: {book.book_title}, Автор: {book.author}, '
            f'страниц: {book.number_of_pages}, материал: {book.page_material}, зарезервирована'
        )
    else:
        print(
            f'Название: {book.book_title}, Автор: {book.author}, страниц: {book.number_of_pages},'
            f' материал: {book.page_material}'
        )


book_information(book1)
book_information(book2)
book_information(book3)
book_information(book4)
book_information(book5)
print('=' * 100)


class SchoolBooks(Book):
    def __init__(self, book_title, author, number_of_pages, isbn, reserve, subject, klass, assignments):
        super().__init__(book_title, author, number_of_pages, isbn, reserve)
        self.subject = subject
        self.assignments = assignments
        self.klass = klass


textbook1 = SchoolBooks('Информатика для старшей школы', 'Иванов', 255, 5678658, True, 'Информатика', 9, True)
textbook2 = SchoolBooks('Английский для старшей школы', 'Петров', 342, 23342, False, 'Английский язык', 8, True)
textbook3 = SchoolBooks('Математика для старшей школы', 'Сидоров', 311, 12312, False, 'Математика', 7, True)


def school_books_information(school_books):
    if school_books.reserve:
        print(
            f'Название: {school_books.book_title}, Автор: {school_books.author}, '
            f'страниц: {school_books.number_of_pages}, предмет: {school_books.subject}, '
            f'класс: {school_books.klass} зарезервирована'
        )
    else:
        print(
            f'Название: {school_books.book_title}, Автор: {school_books.author}, '
            f'страниц: {school_books.number_of_pages}, предмет: {school_books.subject}, '
            f'класс: {school_books.klass} '
        )


school_books_information(textbook1)
school_books_information(textbook2)
school_books_information(textbook3)
