#! python3

from enum import Enum
from Time import Time, Weekday

DEFAULT_ITEMS = {"Burger": 10.99,
                 "Fries": 2.99,
                 "Shake": 3.99,
                 "Salad": 5.99,
                 "Wings": 7.99,
                 "Pizza": 11.99,
                 "Pasta": 8.99,
                 "Soda": 1.99,
                 "Water": 0.00}

DEFAULT_OPENING_HOURS = {Weekday(0): (Time(12, 0), Time(20, 0)),
                         Weekday(1): (Time(12, 0), Time(20, 0)),
                         Weekday(2): (Time(12, 0), Time(20, 0)),
                         Weekday(3): (Time(12, 0), Time(20, 0)),
                         Weekday(4): (Time(12, 0), Time(20, 0)),
                         Weekday(5): (Time(0, 0), Time(0, 0)),
                         Weekday(6): (Time(0, 0), Time(0, 0))}


class OrderStatus(Enum):
    """Enum class for order status"""
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCLED = 3

    def __str__(self) -> str:
        return self.name


class Order():
    """Order class to keep track of orders"""
    number_of_orders = 1

    def __init__(self, customer_name: str, order_items: list = [], items: dict = DEFAULT_ITEMS):
        self.order_number = Order.number_of_orders
        Order.number_of_orders += 1
        self.customer_name = customer_name
        self.order_items = order_items
        self.total_amount = sum([items[item] for item in self.order_items])
        self.status = OrderStatus.NEW

    def get_customer_name(self) -> str:
        return self.customer_name

    def get_items(self) -> list:
        return self.order_items

    def add_item(self, item: str, items: dict = DEFAULT_ITEMS):
        self.order_items.append(item)
        self.total_amount += items[item]

    def remove_item(self, item: str, items: dict = DEFAULT_ITEMS):
        self.order_items.remove(item)
        self.total_amount -= items[item]

    def get_total(self) -> float:
        return self.total_amount

    def get_status(self) -> OrderStatus:
        return self.status

    def set_status(self, status: OrderStatus):
        self.status = status

    def __str__(self) -> str:
        print(f"Order #{self.order_number} by {self.customer_name}, total_amount: {self.total_amount}, status: {self.status}")
        print("Items:")
        for item in self.order_items:
            print(f"\t{item}")
        return ""


class Restaurant():
    """A simple attempt to model a restaurant"""

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = DEFAULT_ITEMS
        self.opening_hours = DEFAULT_OPENING_HOURS
        self.orders_list = []

    def get_name(self) -> str:
        return self.restaurant_name

    def get_items(self) -> dict:
        return self.items

    def get_opening_hours(self) -> dict:
        return self.opening_hours

    def get_opening_hours_day(self, day: Weekday) -> tuple:
        return self.opening_hours[day]

    def set_opening_hours(self, day: Weekday, opening_time: Time, closing_time: Time) -> None:
        self.opening_hours[day] = (opening_time, closing_time)

    def get_open_days(self) -> int:
        return [day for day in self.opening_hours if is_open(self.opening_hours[day])]

    def get_num_open_hours(self) -> Time:
        sum = Time(0, 0)
        for day in self.opening_hours:
            opening_time, closing_time = self.get_opening_hours_day(day)
            sum += closing_time - opening_time
        return sum

    def get_orders(self) -> list:
        return self.orders_list

    def add_order(self, order: Order) -> None:
        self.orders_list.append(order)

    def get_order(self, order_number: int) -> Order:
        for order in self.orders_list:
            if order.order_number == order_number:
                return order
        return None


def is_open(opening_hours: tuple) -> bool:
    """Check if the restaurant is open given the opening hours"""
    if (opening_hours[1] - opening_hours[0]):
        return True
    return False