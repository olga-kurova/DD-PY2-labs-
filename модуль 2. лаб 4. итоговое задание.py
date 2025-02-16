from typing import Union


class Animal:
    """
    Базовый класс, представляющий животное.

    Атрибуты:
        name (str): Имя животного.
        species (str): Вид животного (млекопитающее, птица).
        age (int): Возраст животного.
        _weight (float): Вес животного (в кг).
    Методы:
        make_sound(): Издает звук, характерный для животного.
        eat(food: str) -> str:  Животное ест определенный вид пищи.
        get_weight() -> float:  Возвращает вес животного.
        set_weight(new_weight: float) -> None: Устанавливает вес животного.
        __str__(): Возвращает строковое представление объекта.
        __repr__(): Возвращает строковое представление объекта для отладки.
    """

    def __init__(self, name: str, species: str, age: int, weight: float) -> None:
        """
        Конструктор класса Animal.

        Args:
            name (str): Имя животного.
            species (str): Вид животного.
            age (int): Возраст животного.
            weight (float): Вес животного.
        """
        self.name = name
        self.species = species
        self.age = age
        self._weight = weight

    def make_sound(self) -> str:
        """
        Издает звук, характерный для животного.

        Returns:
            str: Строка, представляющая звук животного.
        """
        return "Generic animal sound"

    def eat(self, food: str) -> str:
        """
        Животное ест определенный вид пищи.

        Args:
            food (str): Тип пищи.

        Returns:
            str: Сообщение о том, что животное ест пищу.
        """
        return f"{self.name} is eating {food}"

    def get_weight(self) -> float:
        """
        Возвращает вес животного.

        Returns:
            float: Вес животного.
        """
        return self._weight

    def set_weight(self, new_weight: float) -> None:
        """
        Устанавливает вес животного.

        Args:
            new_weight (float): Новый вес животного.
        """
        if new_weight >= 0:
            self._weight = new_weight
        else:
            print("Вес не может быть отрицательным.")

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Строковое представление объекта.
        """
        return f"{self.name} is a {self.species} aged {self.age} and weighs {self._weight} kg."

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Returns:
            str: Строковое представление объекта для отладки.
        """
        return f"Animal(name='{self.name}', species='{self.species}', age={self.age}, weight={self._weight})"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.

    Атрибуты:
        name (str): Имя собаки.
        breed (str): Порода собаки.
        age (int): Возраст собаки.
        weight (float): Вес собаки.

    Методы:
        bark() -> str: Собака лает.
        fetch(item: str) -> str: Собака приносит предмет.
        make_sound() -> str:  Перегруженный метод. Собака лает.
        __str__(): Перегруженный метод.  Возвращает строковое представление объекта Dog.
        __repr__(): Перегруженный метод. Возвращает строковое представление объекта Dog для отладки.
    """

    def __init__(self, name: str, breed: str, age: int, weight: float) -> None:
        """
        Конструктор класса Dog.

        Args:
            name (str): Имя собаки.
            breed (str): Порода собаки.
            age (int): Возраст собаки.
            weight (float): Вес собаки.
        """
        super().__init__(name, "Dog", age, weight)  # Расширяем конструктор базового класса
        self.breed = breed

    def bark(self) -> str:
        """
        Собака лает.

        Returns:
            str: Строка, представляющая лай собаки.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Собака приносит предмет.

        Args:
            item (str): Предмет, который собака приносит.

        Returns:
            str: Сообщение о том, что собака принесла предмет.
        """
        return f"{self.name} is fetching the {item}"

    def make_sound(self) -> str:
        """
        Перегруженный метод. Собака лает.

        Перегрузка выполнена, так как звук, издаваемый собакой, отличается
        от звука, издаваемого другими животными.

        Returns:
            str: Строка, представляющая лай собаки.
        """
        return "Woof woof!"

    def __str__(self) -> str:
        """
        Перегруженный метод.  Возвращает строковое представление объекта Dog.

        Перегрузка выполнена для добавления информации о породе собаки.

        Returns:
            str: Строковое представление объекта Dog.
        """
        return f"{self.name} is a {self.breed} Dog aged {self.age} and weighs {self._weight} kg."

    def __repr__(self) -> str:
        """
        Перегруженный метод. Возвращает строковое представление объекта Dog для отладки.

        Перегрузка выполнена для добавления информации о породе собаки.

        Returns:
            str: Строковое представление объекта Dog для отладки.
        """
        return f"Dog(name='{self.name}', breed='{self.breed}', age={self.age}, weight={self._weight})"


if __name__ == "__main__":
    animal = Animal("Generic", "Mammal", 5, 20.5)
    print(animal)
    print(repr(animal))
    print(animal.make_sound())
    print(animal.eat("grass"))
    print(f"Вес животного: {animal.get_weight()}")
    animal.set_weight(22.0)
    print(f"Вес животного после изменения: {animal.get_weight()}")

    dog = Dog("Buddy", "Golden Retriever", 3, 30.0)
    print(dog)
    print(repr(dog))
    print(dog.bark())
    print(dog.fetch("ball"))
    print(dog.make_sound())  # Перегруженный метод
    print(dog.eat("meat"))  # Унаследованный метод
    print(f"Вес собаки: {dog.get_weight()}")
    dog.set_weight(32.5)
    print(f"Вес собаки после изменения: {dog.get_weight()}")
