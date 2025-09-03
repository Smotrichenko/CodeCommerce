import pytest

from src.category import BaseContainer, Category, Order
from src.product import BaseProduct, Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Тестовое описание"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Тестовая категория"
    assert sample_category.description == "Тестовое описание"
    assert len(sample_category.products) == 2

    # Проверяем через список строк (если products возвращает строки)
    products_list = sample_category.products
    assert isinstance(products_list, list)

    # Проверяем содержимое первого товара
    assert "Товар 1" in products_list[0]
    assert "100 руб." in products_list[0]
    assert "Остаток: 5 шт." in products_list[0]

    # Проверяем содержимое второго товара
    assert "Товар 2" in products_list[1]
    assert "200 руб." in products_list[1]
    assert "Остаток: 3 шт." in products_list[1]


def test_category_count(sample_category):
    assert Category.category_count == 1
    Category("Новая категория", "Описание", [])
    assert Category.category_count == 2


def test_product_count(sample_category):
    assert Category.product_count == 2
    new_product = Product("Новый товар", "Описание", 300, 1)
    Category("Новая категория", "Описание", [new_product])
    assert Category.product_count == 3


def test_empty_category_product_count():
    """Тест счетчика товаров для пустой категории"""
    Category.category_count = 0
    Category.product_count = 0

    empty_category = Category("Пустая", "Описание", [])
    assert Category.product_count == 0
    assert len(empty_category.products) == 0


def test_new_product_creation():
    product_data = {"name": "New Product", "description": "New Description", "price": 500.0, "quantity": 7}
    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.price == 500.0
    assert product.quantity == 7


def test_new_product_duplicate(sample_products):
    product_data = {"name": "Товар 1", "description": "Новое описание", "price": 300.0, "quantity": 4}
    product = Product.new_product(product_data, sample_products)
    assert product.quantity == 9
    assert product.price == 300.0
    assert product.description == "Новое описание"


def test_add_product(sample_category):
    new_product = Product("New Product", "Desc", 300, 1)
    sample_category.add_product(new_product)
    assert len(sample_category.products) == 3
    assert Category.product_count == 3


def test_add_duplicate_product(sample_category, sample_products):
    duplicate_product = sample_products[0]
    initial_count = sample_products[0].quantity
    sample_category.add_product(duplicate_product)
    assert len(sample_category.products) == 2
    assert sample_category.products[0].endswith(f"{initial_count * 2} шт.")


def test_product_str_representation(sample_product):
    expected_str = "Тестовый товар, 1000.0 руб. Остаток: 10 шт."
    assert str(sample_product) == expected_str


def test_category_str_representation(sample_category):
    expected_str = "Тестовая категория, количество продуктов: 8 шт."
    assert str(sample_category) == expected_str


def test_category_str_empty_category():
    empty_category = Category("Пустая категория", "Нет товаров", [])
    expected_str = "Пустая категория, количество продуктов: 0 шт."
    assert str(empty_category) == expected_str


def test_category_str_with_single_product():
    product = Product("Один товар", "Описание", 500.0, 1)
    category = Category("Одна категория", "Описание", [product])
    expected_str = "Одна категория, количество продуктов: 1 шт."
    assert str(category) == expected_str


def test_product_addition_basic(sample_products):
    product1, product2 = sample_products
    result = product1 + product2
    expected = (100 * 5) + (200 * 3)
    assert result == expected


def test_product_addition_with_itself(sample_product):
    result = sample_product + sample_product
    expected = (1000.0 * 10) * 2
    assert result == expected


def test_product_addition_different_values():
    product1 = Product("Дорогой", "Описание", 5000.0, 2)  # 10000
    product2 = Product("Дешевый", "Описание", 100.0, 20)  # 2000
    result = product1 + product2
    expected = 10000 + 2000
    assert result == expected


def test_product_addition_zero_quantity():
    product1 = Product("Товар 1", "Описание", 100.0, 0)  # 0
    product2 = Product("Товар 2", "Описание", 200.0, 5)  # 1000
    result = product1 + product2
    expected = 0 + 1000
    assert result == expected


def test_product_addition_type_error(sample_product):
    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
        sample_product + "not a product"


def test_product_addition_commutative(sample_products):
    product1, product2 = sample_products
    result1 = product1 + product2
    result2 = product2 + product1
    assert result1 == result2  # Должно быть одинаково


def test_smartphone_initialization(sample_smartphone):
    """Тест создания смартфона"""
    assert sample_smartphone.name == "Тестовый смартфон"
    assert sample_smartphone.price == 50000.0
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == 4.5
    assert sample_smartphone.model == "Test Model"
    assert sample_smartphone.memory == 128
    assert sample_smartphone.color == "Черный"


def test_lawn_grass_initialization(sample_lawn_grass):
    """Тест создания газонной травы"""
    assert sample_lawn_grass.name == "Тестовая трава"
    assert sample_lawn_grass.price == 1500.0
    assert sample_lawn_grass.quantity == 20
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == "14 дней"
    assert sample_lawn_grass.color == "Зеленый"


def test_smartphone_inheritance(sample_smartphone):
    """Тест что смартфон наследует от Product"""
    assert isinstance(sample_smartphone, Product)
    assert hasattr(sample_smartphone, "name")
    assert hasattr(sample_smartphone, "price")
    assert hasattr(sample_smartphone, "quantity")


def test_lawn_grass_inheritance(sample_lawn_grass):
    """Тест что газонная трава наследует от Product"""
    assert isinstance(sample_lawn_grass, Product)
    assert hasattr(sample_lawn_grass, "name")
    assert hasattr(sample_lawn_grass, "price")
    assert hasattr(sample_lawn_grass, "quantity")


def test_smartphone_str_representation(sample_smartphone):
    """Тест строкового представления смартфона"""
    result = str(sample_smartphone)
    assert "Тестовый смартфон" in result
    assert "50000.0 руб." in result
    assert "128GB" in result
    assert "Черный" in result


def test_lawn_grass_str_representation(sample_lawn_grass):
    """Тест строкового представления газонной травы"""
    result = str(sample_lawn_grass)
    assert "Тестовая трава" in result
    assert "1500.0 руб." in result
    assert "Россия" in result
    assert "14 дней" in result


def test_smartphone_addition_same_class(sample_smartphones):
    """Тест сложения смартфонов одинакового класса"""
    phone1, phone2 = sample_smartphones
    result = phone1 + phone2
    expected = (30000 * 3) + (40000 * 2)  # 90000 + 80000 = 170000
    assert result == expected


def test_lawn_grass_addition_same_class(sample_lawns):
    """Тест сложения газонной травы одинакового класса"""
    grass1, grass2 = sample_lawns
    result = grass1 + grass2
    expected = (1000 * 10) + (1200 * 8)  # 10000 + 9600 = 19600
    assert result == expected


def test_product_addition_same_class(sample_products):
    """Тест сложения обычных продуктов одинакового класса"""
    product1, product2 = sample_products
    result = product1 + product2
    expected = (100 * 5) + (200 * 3)  # 500 + 600 = 1100
    assert result == expected


def test_smartphone_addition_different_class(sample_smartphone, sample_lawn_grass):
    """Тест ошибки при сложении смартфона и газонной травы"""
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов"):
        sample_smartphone + sample_lawn_grass


def test_product_addition_with_smartphone(sample_product, sample_smartphone):
    """Тест ошибки при сложении обычного продукта и смартфона"""
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов"):
        sample_product + sample_smartphone


def test_product_addition_with_lawn_grass(sample_product, sample_lawn_grass):
    """Тест ошибки при сложении обычного продукта и газонной травы"""
    with pytest.raises(TypeError, match="Можно складывать только товары из одинаковых классов"):
        sample_product + sample_lawn_grass


def test_add_smartphone_to_category(sample_category, sample_smartphone):
    """Тест добавления смартфона в категорию"""
    initial_count = len(sample_category.products)
    sample_category.add_product(sample_smartphone)
    assert len(sample_category.products) == initial_count + 1
    assert Category.product_count == 3


def test_add_lawn_grass_to_category(sample_category, sample_lawn_grass):
    """Тест добавления газонной травы в категорию"""
    initial_count = len(sample_category.products)
    sample_category.add_product(sample_lawn_grass)
    assert len(sample_category.products) == initial_count + 1
    assert Category.product_count == 3


def test_add_invalid_object_to_category(sample_category):
    """Тест ошибки при добавлении не-продукта в категорию"""
    with pytest.raises(ValueError, match="Можно добавлять только объекты класса Product или его наследников"):
        sample_category.add_product("not a product")


def test_add_number_to_category(sample_category):
    """Тест ошибки при добавлении числа в категорию"""
    with pytest.raises(ValueError, match="Можно добавлять только объекты класса Product или его наследников"):
        sample_category.add_product(123)


def test_add_list_to_category(sample_category):
    """Тест ошибки при добавлении списка в категорию"""
    with pytest.raises(ValueError, match="Можно добавлять только объекты класса Product или его наследников"):
        sample_category.add_product([1, 2, 3])


def test_category_with_mixed_products(sample_smartphones, sample_lawns):
    """Тест категории со смешанными типами продуктов"""
    mixed_products = sample_smartphones + sample_lawns
    category = Category("Смешанная категория", "Разные товары", mixed_products)
    assert len(category.products) == 4
    assert "Смартфон 1" in category.products[0]
    assert "Трава 1" in category.products[2]


def test_category_str_with_mixed_products(sample_smartphones, sample_lawns):
    """Тест строкового представления категории со смешанными товарами"""
    mixed_products = sample_smartphones + sample_lawns
    category = Category("Смешанная категория", "Разные товары", mixed_products)
    total_quantity = 3 + 2 + 10 + 8  # 23 товара
    assert str(category) == f"Смешанная категория, количество продуктов: {total_quantity} шт."


def test_base_product_abstract():
    """Тест что BaseProduct является абстрактным"""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100, 10)


def test_repr_mixin(capsys):
    """Тест миксина для вывода информации"""
    product = Product("Test", "Desc", 100, 5)
    captured = capsys.readouterr()
    assert "Product('Test', 'Desc', 100, 5)" in captured.out


def test_order_creation(sample_product):
    """Тест создания заказа"""
    order = Order("Мой заказ", "Первый заказ", sample_product, 3)
    assert order.name == "Мой заказ"
    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_price == 1000 * 3  # 3000


def test_order_str(sample_product):
    """Тест строкового представления заказа"""
    order = Order("Тестовый заказ", "Описание", sample_product, 2)
    result = str(order)
    assert "Заказ: Тестовый заказ" in result
    assert "Товар: Тестовый товар" in result
    assert "Количество: 2" in result
    assert "Итого: 2000.0 руб." in result


def test_base_container_inheritance():
    """Тест что Category и Order наследуют от BaseContainer"""
    category = Category("Test", "Desc")
    order = Order("Test", "Desc", Product("T", "D", 100, 1), 1)
    assert isinstance(category, BaseContainer)
    assert isinstance(order, BaseContainer)
