# Ввод данных о книгах
my_books = [
    {"id": 1, "name": "name1", "pages": 123},
    {"id": 2, "name": "name2", "pages": 1234},
]

# Создание класса
class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'

if __name__ == '__main__':
    list_books = [Book(**book_dict) for book_dict in my_books]

    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
