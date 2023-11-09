#! python3

from Restaurants import Restaurant, Order, OrderStatus


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
    my_order2 = Order("Peder", ["Shake", "Salad"], BagBite.get_items())
    BagBite.add_order(my_order)
    BagBite.add_order(my_order1)
    BagBite.add_order(my_order2)
    my_order1.set_status(OrderStatus.IN_PROGRESS)
    for order in BagBite.orders_list:
        print(order)

    print(f"Average opening hours per week: {BagBite.avg_open_hours_week()}")
    print(f"Average orders per day: {BagBite.avg_orders_per_day()}")


if __name__ == "__main__":
    Main()
