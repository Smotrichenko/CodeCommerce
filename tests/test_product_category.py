from src.product_category import Category, Product
import pytest

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