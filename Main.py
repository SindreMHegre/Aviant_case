#! python3

from Restaurants import *
from Time import Weekday


def Main():
    BagBite = Restaurant("BagBite")
    print("Restaurant: BagBite")
    print(f"Name: {BagBite.get_name()}")
    print(f"Items: {BagBite.get_items()}")
    print(f"Opening Hours: {BagBite.get_opening_hours()}")
    print(f"Orders: {BagBite.orders_list}")

    my_order = Order("John", ["Burger", "Fries"], BagBite.get_items())
    my_order1 = Order("Sindre")
    my_order1.add_item("Pizza", BagBite.get_items())
    BagBite.add_order(my_order)
    BagBite.add_order(my_order1)
    my_order1.set_status(OrderStatus.IN_PROGRESS)
    for order in BagBite.orders_list:
        print(order)

    print(BagBite.get_open_days())
    print(BagBite.get_num_open_hours())


if __name__ == "__main__":
    Main()
