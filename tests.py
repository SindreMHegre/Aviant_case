#! python3

"""Tests for the Restaurant and order classes"""

from restaurants import Restaurant, Order, OrderStatus


def test_restaurant() -> None:
    BagBite = Restaurant("BagBite")
    print("Restaurant: BagBite")
    print(f"Name: {BagBite.get_name()}")
    print(f"Items: {BagBite.get_items()}")
    print(f"Opening Hours: {BagBite.get_opening_hours()}")
    print(f"Orders: {BagBite.orders_list}")


def test_order() -> None:
    BagBite = Restaurant("BagBite")
    my_order1 = Order("Sindre")
    my_order1.add_item("Pizza", BagBite.get_items())
    my_order1.set_status(OrderStatus.IN_PROGRESS)
    my_order = Order("John", ["Burger", "Fries"], BagBite.get_items())

    BagBite.add_order(my_order)
    BagBite.add_order(my_order1)

    for order in BagBite.orders_list:
        print(order)
