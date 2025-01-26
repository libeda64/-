my_books = [
    {"id": 1, "name": "name1", "pages": 123},
    {"id": 2, "name": "name2", "pages": 1234},
]


# Создание класса Book
class Book:

    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages


# Создание класса Library

class Library:
    def __init__(self, books = None):
        if books is None:
            books = []
        self.books = books
    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [Book(**book_dict) for book_dict in my_books]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
