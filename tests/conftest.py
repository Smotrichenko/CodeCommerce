import pytest

from src.product_category import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture(autouse=True)
def reset_category_counterse():
    """
    Перед каждым тестом сбрасывает атрибуты
    category_count и product_count у класса Category.
    """
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture()
def sample_smartphone():
    return Smartphone(
        name="Тестовый смартфон",
        description="Тестовое описание",
        price=50000.0,
        quantity=5,
        efficiency=4.5,
        model="Test Model",
        memory=128,
        color="Черный",
    )


@pytest.fixture()
def sample_lawn_grass():
    return LawnGrass(
        name="Тестовая трава",
        description="Тестовое описание",
        price=1500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )


@pytest.fixture()
def sample_smartphones():
    return [
        Smartphone("Смартфон 1", "Описание 1", 30000, 3, 4.0, "Model A", 64, "Синий"),
        Smartphone("Смартфон 2", "Описание 2", 40000, 2, 4.5, "Model B", 128, "Черный"),
    ]


@pytest.fixture()
def sample_lawns():
    return [
        LawnGrass("Трава 1", "Описание 1", 1000, 10, "Россия", "10 дней", "Зеленый"),
        LawnGrass("Трава 2", "Описание 2", 1200, 8, "Германия", "7 дней", "Темно-зеленый"),
    ]
