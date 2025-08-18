import pytest

from src.product_category import Category, Product


@pytest.fixture()
def sample_product():
    return Product(name="Тестовый товар", description="Тестовое описание", price=1000.0, quantity=10)


@pytest.fixture
def sample_products():
    return [Product("Товар 1", "Описание 1", 100, 5), Product("Товар 2", "Описание 2", 200, 3)]


@pytest.fixture()
def sample_category(sample_products):
    Category.category_count = 0
    Category.product_count = 0
    return Category(name="Тестовая категория", description="Тестовое описание", products=sample_products)
