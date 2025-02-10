class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
        def name(self) -> str:
            """Getter для названия книги."""
            return self._name

    @property
        def author(self) -> str:
            """Getter для автора книги."""
            return self._author


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} (Количество страниц: {self.pages})"

    @property
    def pages(self) -> int:
        """Getter для количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        """Setter для количества страниц."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} (Продолжительность: {self.duration} мин.)"

    @property
    def duration(self) -> float:
        """Getter для продолжительности."""
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        """Setter для продолжительности."""
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = duration
