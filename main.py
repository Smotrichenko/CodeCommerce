from src.category import Category, Order
from src.product import Product, ZeroQuantityError

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(
            "Возникла ошибка ZeroQuantityError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
        print(f"Сообщение ошибки: {e}")
    else:
        print("Не возникла ошибка при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.get_average_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.get_average_price())

    order = Order("Мой первый заказ", "Заказ смартфона", product1, 2)
    print(order)
    print(f"Итоговая стоимость: {order.total_price} руб.")
