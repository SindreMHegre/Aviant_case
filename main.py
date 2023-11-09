#! python3

from restaurants import Restaurant, Order, OrderStatus
from webpage import create_webpage


def init_mock_restaurant() -> Restaurant:
    BagBite = Restaurant("BagBite")

    my_order = Order("John", ["Burger", "Fries"], BagBite.get_items())
    my_order1 = Order("Sindre", ["Pizza"], BagBite.get_items())
    my_order2 = Order("Peder", ["Shake", "Salad"], BagBite.get_items())
    my_order1.set_status(OrderStatus.IN_PROGRESS)
    BagBite.add_order(my_order)
    BagBite.add_order(my_order1)
    BagBite.add_order(my_order2)
    return BagBite


def Main():
    BagBite = init_mock_restaurant()
    web_app = create_webpage(BagBite)
    web_app.run(debug=True)


if __name__ == "__main__":
    Main()
