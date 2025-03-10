from typing import Any
import doctest

class Table():
    """
    Абстрактный класс, описывающий стол.
    """

    def __init__(self, material: str, number_of_legs: int):
        if number_of_legs <= 0:
            raise ValueError("Количество ножек должно быть больше нуля.")
        self.material = material
        self.number_of_legs = number_of_legs

    
    def assemble(self) -> None:
        """
        Метод для сборки стола.

        Returns:
            None

        Пример использования:
         table.assemble()
        """
        pass

    
    def move(self, new_position: str) -> None:
        """
        Переместить стол в новое положение.

        Args:
            new_position (str): Новое местоположение стола.

        Returns:
            None

        Пример использования:
         table.move("Living Room")
        """
        pass

    
    def clean(self) -> None:
        """
        Очистить стол.

        Returns:
            None

        Пример использования:
         table.clean()
        """
        pass

class Tree():
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.age = age

    
    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева.

        Args:
            years (int): Количество лет для увеличения возраста.

        Returns:
            None

        Пример использования:
         Tree.grow(5)
        """
        pass

    
    def photosynthesize(self) -> None:
        """
        Выполнить процесс фотосинтеза.

        Returns:
            None

        Пример использования:
         Tree.photosynthesize()
        """
        pass

    
    def shed_leaves(self) -> None:
        """
        Сбрасывать листья.

        Returns:
            None

        Пример использования:
         Tree.shed_leaves()
        """
        pass

class Stack():
    """
    Абстрактный класс, описывающий стек.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Вместимость должна быть больше нуля.")
        self.capacity = capacity
        self.items = []

    
    def push(self, item: Any) -> None:
        """
        Добавить элемент в стек.

        Args:
            item (Any): Элемент для добавления.

        Returns:
            None

        Пример использования:
         stack.push(5)
        """
        pass

    
    def pop(self) -> Any:
        """
        Удалить и вернуть верхний элемент из стека.

        Returns:
            Any: Верхний элемент стека.

        Пример использования:
         top = stack.pop()
        """
        pass

    
    def peek(self) -> Any:
        """
        Вернуть верхний элемент из стека, не удаляя его.

        Returns:
            Any: Верхний элемент стека.

        Пример использования:
         top = stack.peek()
        """
        pass
if __name__ == "__main__":
    doctest.testmod()