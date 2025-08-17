from typing import Dict, List


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Товар: {self.name}, Описание: {self.description}, Цена: {self.price} руб. Остаток: {self.quantity} шт."
        )

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

        return cls(name, description, price, quantity)

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

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты класса Product")

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


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
