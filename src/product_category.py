from typing import Dict, List


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление для пользователя: Название, Цена и Остаток"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов: возвращает общую стоимость всех товаров"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары из одинаковых классов")

        return (self.price * self.quantity) + (other.price * other.quantity)

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

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self._price:
            confirm = input(f"Цена снижается с {self._price} до {new_price}. Подтвердите (y/n): ")
            if confirm.lower() == "y":
                self._price = new_price
        else:
            self._price = new_price


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


class Category:
    """Класс для представления категории продукта"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def __str__(self):
        """Строковое представление категории: Название и Общее количество товаров"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product или его наследников")

        existing_product = next((i for i in self.__products if i.name == product.name), None)
        if existing_product:
            existing_product.quantity += product.quantity
            if product.price > existing_product.price:
                existing_product.price = product.price
                existing_product.description = product.description
        else:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        """Возвращает список строк с информацией о продуктах"""
        return [str(product) for product in self.__products]

    def __len__(self):
        return len(self.__products)
