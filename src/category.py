from src.product import Product


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
