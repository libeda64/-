class Book:
    """Просто книга."""
    def __init__(self, name: str, author: str):
        self._name: str = name
        self._author: str = author

    def __str__(self) -> str:
        return f"Книга {self.name}, автор {self.author}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Страниц должно быть положительное число")
        self._pages = value

    def __str__(self) -> str:
        return f"Книга {self.name}, автор {self.author}, страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("Длительность должна быть положительной")
        self.duration: float = float(duration)

    def __str__(self) -> str:
        return f"Книга {self.name}, автор {self.author}, длительность {self.duration} ч."
