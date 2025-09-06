from abc import ABC, abstractmethod

from src.product import Product, ZeroQuantityError


class BaseContainer(ABC):
    """Абстрактный класс для категорий продуктов"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        pass


class Category(BaseContainer):
    """Класс для представления категории продукта"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        super().__init__(name, description)
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

        try:
            if not isinstance(product, Product):
                raise ValueError("Можно добавлять только объекты класса Product или его наследников")

            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")

            existing_product = next((i for i in self.__products if i.name == product.name), None)
            if existing_product:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                    existing_product.description = product.description
            else:
                self.__products.append(product)
                Category.product_count += 1

            print("Товар успешно добавлен")

        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        """Возвращает список строк с информацией о продуктах"""

        return [str(product) for product in self.__products]

    def __len__(self):
        return len(self.__products)

    def get_average_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории"""

        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return f"{round(total_price / total_quantity, 2)} руб."
        except ZeroDivisionError:
            return 0.0


class Order(BaseContainer):
    def __init__(self, name: str, description: str, product: Product, quantity: int):
        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Нельзя заказать товар с нулевым количеством")
            if quantity == 0:
                raise ZeroQuantityError("Количество товара в заказе не может быть нулевым")
            super().__init__(name, description)
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity

            print("Заказ успешно создан")

        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка создания заказа завершена")

    def __str__(self):
        return (
            f"Заказ: {self.name}, Товар: {self.product.name}, "
            f"Количество: {self.quantity}, Итого: {self.total_price} руб. "
        )
