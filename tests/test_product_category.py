from src.product_category import Category, Product


def test_product_initialization(sample_product):
    assert sample_product.name == "Тестовый товар"
    assert sample_product.description == "Тестовое описание"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 10


def test_category_initialization(sample_category, sample_products):
    assert sample_category.name == "Тестовая категория"
    assert sample_category.description == "Тестовое описание"
    assert len(sample_category.products) == 2
    assert sample_category.products[0].name == "Товар 1"
    assert sample_category.products[1].name == "Товар 2"


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


def test_product_repr_representation(sample_product):
    """Тест repr представления продукта"""
    expected_repr = "Товар: Тестовый товар, Описание: Тестовое описание, Цена: 1000.0 руб."
    assert repr(sample_product) == expected_repr
