from abc import ABC, abstractmethod
from typing import Dict, List


class ReprMixin:
    """Миксин для вывода информации о создании объекта"""

    def __repr__(self):
        return f"('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict, existing_products: List = None):
        pass


class Product(BaseProduct, ReprMixin):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(f"{self.__class__.__name__}{self.__repr__()}")

    def __repr__(self):
        return f"('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self):
        """Строковое представление для пользователя: Название, Цена и Остаток"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов: возвращает общую стоимость всех товаров"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары из одинаковых классов")

        return (self.__price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
            if confirm.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict, existing_products: List = None):
        """Создает новый продукт или обновляет существующий"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if existing_products:
            for product in existing_products:
                if product.name.lower() == name.lower():
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                        product.description = description
                    return product

        return cls(**product_data)


class Smartphone(Product):
    """Класс для смартфонов - наследуется от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона"""
        return (
            f"{self.name} ({self.model}), {self.price} руб. "
            f"Память: {self.memory}GB, Цвет: {self.color} "
            f"Остаток: {self.quantity} шт. "
        )


class LawnGrass(Product):
    """Класс для газонной травы - наследуется от Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)

        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление для газонной травы"""
        return (
            f"{self.name}, {self.price} руб. "
            f"Страна: {self.country}, Прорастание: {self.germination_period}. "
            f"Остаток: {self.quantity} шт."
        )
