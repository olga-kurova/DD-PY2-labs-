from typing import Union, List
import doctest


class Book:
    """
    Абстрактный класс, описывающий книгу.

    Attributes:
        title (str): Название книги.
        author (str): Автор книги.
        page_count (int): Количество страниц в книге.
    """

    def __init__(self, title: str, author: str, page_count: int):
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.title = title
        self.author = author
        self.page_count = page_count

    def read(self, pages_read: int) -> None:
        """
        Увеличивает количество прочитанных страниц в книге.

        Args:
          pages_read (int): Количество прочитанных страниц.

        Examples:
          >>> book = Book("Example Book", "John Doe", 300)
          >>> book.read(50)
        """
        ...

    def write_review(self, review: str) -> None:
        """
        Добавляет отзыв о книге.

        Args:
          review (str): Отзыв о книге.

        Examples:
          >>> book = Book("Example Book", "John Doe", 300)
          >>> book.write_review("Great book!")
        """
        ...

    def get_reading_progress(self) -> float:
        """
        Возвращает процент прочитанных страниц.

        Returns:
          float: Процент прочитанных страниц.

        Examples:
          >>> book = Book("Example Book", "John Doe", 300)
          >>> book.read(150)
          >>> book.get_reading_progress()
          50.0
        """
        ...


class Smartphone:
    """
    Абстрактный класс, описывающий смартфон.

    Attributes:
      model (str): Модель смартфона.
      os (str): Операционная система смартфона.
      storage_capacity (int): Объем памяти смартфона в гигабайтах.
    """

    def __init__(self, model: str, os: str, storage_capacity: int):
        if not isinstance(model, str):
            raise TypeError("Модель смартфона должна быть строкой")
        if not isinstance(os, str):
            raise TypeError("Операционная система должна быть строкой")
        if not isinstance(storage_capacity, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if storage_capacity <= 0:
            raise ValueError("Объем памяти должен быть положительным числом")

        self.model = model
        self.os = os
        self.storage_capacity = storage_capacity

    def install_app(self, app_name: str) -> None:
        """
        Устанавливает приложение на смартфон.

        Args:
          app_name (str): Название устанавливаемого приложения.

        Examples:
           >>> phone = Smartphone("Example Phone", "Android", 128)
           >>> phone.install_app("My App")
        """
        ...

    def make_call(self, phone_number: str) -> None:
        """
        Совершает вызов на указанный номер.

        Args:
          phone_number (str): Номер телефона для вызова.

        Examples:
           >>> phone = Smartphone("Example Phone", "Android", 128)
           >>> phone.make_call("+1234567890")
        """
        ...

    def get_available_storage(self) -> int:
        """
        Возвращает оставшееся свободное место на смартфоне.

        Returns:
          int: Оставшееся свободное место на смартфоне.

        Examples:
          >>> phone = Smartphone("Example Phone", "Android", 128)
          >>> phone.install_app("My App")
          >>> phone.get_available_storage()
          127
        """
        ...


class SocialNetwork:
    """
    Абстрактный класс, описывающий социальную сеть.

    Attributes:
      name (str): Название социальной сети.
      user_count (int): Количество пользователей в социальной сети.
      posts_count (int): Количество публикаций в социальной сети.
    """

    def __init__(self, name: str, user_count: int, posts_count: int):
        if not isinstance(name, str):
            raise TypeError("Название социальной сети должно быть строкой")
        if not isinstance(user_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if not isinstance(posts_count, int):
            raise TypeError("Количество публикаций должно быть целым числом")
        if user_count <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом")
        if posts_count < 0:
            raise ValueError("Количество публикаций не может быть отрицательным числом")

        self.name = name
        self.user_count = user_count
        self.posts_count = posts_count

    def add_user(self, user_name: str) -> None:
        """
        Добавляет нового пользователя в социальную сеть.

        Args:
          user_name (str): Имя нового пользователя.

        Examples:
          >>> network = SocialNetwork("ExampleNet", 1000, 5000)
          >>> network.add_user("New User")
        """
        ...

    def create_post(self, text: str) -> None:
        """
        Создает новую публикацию в социальной сети.

        Args:
          text (str): Текст публикации.

        Examples:
          >>> network = SocialNetwork("ExampleNet", 1000, 5000)
          >>> network.create_post("Hello, world!")
        """
        ...

    def get_average_posts_per_user(self) -> float:
        """
        Возвращает среднее количество публикаций на одного пользователя.

        Returns:
           float: Среднее количество публикаций на одного пользователя.

        Examples:
          >>> network = SocialNetwork("ExampleNet", 1000, 5000)
          >>> network.get_average_posts_per_user()
          5.0
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
