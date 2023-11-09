#! python3

from enum import Enum
from datetime import datetime, timedelta, date
from math import ceil

# TODO stop mixing "dates" and "days"

# Mock menu
DEFAULT_ITEMS = {"Burger": 10.99,
                 "Fries": 2.99,
                 "Shake": 3.99,
                 "Salad": 5.99,
                 "Wings": 7.99,
                 "Pizza": 11.99,
                 "Pasta": 8.99,
                 "Soda": 1.99,
                 "Water": 0.00}

# Mock opening hours
DEFAULT_OPENING_HOURS = {date(2023, 11, 13): (datetime(2023, 11, 13, 12, 0), datetime(2023, 11, 13, 20, 0)),
                         date(2023, 11, 14): (datetime(2023, 11, 14, 12, 0), datetime(2023, 11, 14, 20, 0)),
                         date(2023, 11, 15): (datetime(2023, 11, 15, 12, 0), datetime(2023, 11, 15, 20, 0)),
                         date(2023, 11, 16): (datetime(2023, 11, 16, 12, 0), datetime(2023, 11, 16, 20, 0)),
                         date(2023, 11, 17): (datetime(2023, 11, 17, 12, 0), datetime(2023, 11, 17, 20, 0)),
                         date(2023, 11, 18): (datetime(2023, 11, 18, 0, 0), datetime(2023, 11, 18, 0, 0)),
                         date(2023, 11, 19): (datetime(2023, 11, 19, 0, 0), datetime(2023, 11, 19, 0, 0)),
                         date(2023, 11, 20): (datetime(2023, 11, 13, 12, 0), datetime(2023, 11, 13, 20, 0)),
                         date(2023, 11, 21): (datetime(2023, 11, 14, 12, 0), datetime(2023, 11, 14, 20, 0)),
                         date(2023, 11, 22): (datetime(2023, 11, 15, 12, 0), datetime(2023, 11, 15, 20, 0)),
                         date(2023, 11, 23): (datetime(2023, 11, 16, 12, 0), datetime(2023, 11, 16, 20, 0)),
                         date(2023, 11, 24): (datetime(2023, 11, 17, 12, 0), datetime(2023, 11, 17, 20, 0)),
                         date(2023, 11, 25): (datetime(2023, 11, 18, 0, 0), datetime(2023, 11, 18, 0, 0)),
                         date(2023, 11, 26): (datetime(2023, 11, 19, 0, 0), datetime(2023, 11, 19, 0, 0))}


class OrderStatus(Enum):
    """Enum class for order status"""
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CANCLED = 3

    def __str__(self) -> str:
        return self.name

    def __gt__(self, other) -> bool:
        return self.value > other.value


class Order():
    """Order class to keep track of orders"""
    number_of_orders = 1

    def __init__(self, customer_name: str, order_items: list = [], items: dict = DEFAULT_ITEMS):
        self.number = Order.number_of_orders
        Order.number_of_orders += 1
        self.time = datetime.now()
        self.customer_name = customer_name
        self.order_items = order_items
        self.total_amount = sum([items[item] for item in self.order_items])
        self.status = OrderStatus.NEW

    def get_number(self) -> int:
        return self.number

    def get_customer_name(self) -> str:
        return self.customer_name

    def get_time(self) -> datetime:
        return self.time

    def set_time(self, time: datetime):
        self.time = time

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
        order_string = (f"Order #{self.number} by {self.customer_name}"
                        f"\n At {self.time.strftime('%H:%M %d/%m/%Y')}"
                        f"\nTotal_amount: {self.total_amount}$"
                        f"\n Status: {self.status}"
                        f"\nItems:")
        for item in self.order_items:
            order_string += (f"\n\t- {item}")
        return order_string


class Restaurant():
    """Restaurant class to keep track class variables and methods"""

    def __init__(self, restaurant_name, items: dict = DEFAULT_ITEMS, opening_hours: dict = DEFAULT_OPENING_HOURS):
        self.restaurant_name = restaurant_name
        self.items = items
        self.opening_hours = opening_hours
        self.orders_list = []

    def get_name(self) -> str:
        return self.restaurant_name

    def get_items(self) -> dict:
        return self.items

    def get_opening_hours(self) -> dict:
        return self.opening_hours

    def get_opening_hours_date(self, date: date) -> tuple:
        """Returns the opening hours for a given date"""
        return self.opening_hours[date]

    def set_opening_hours(self, date: date, opening_time: datetime, closing_time: datetime) -> None:
        if closing_time < opening_time:
            raise ValueError("Closing time must be after opening time")
        self.opening_hours[date] = (opening_time, closing_time)

    def get_orders(self) -> list:
        return self.orders_list

    def add_order(self, order: Order) -> None:
        self.orders_list.append(order)

    def get_order(self, number: int) -> Order:
        for order in self.orders_list:
            if order.number == number:
                return order
        raise ValueError(f"Found no order with order number {number}")

    def get_open_dates(self) -> list:
        """Returns a list of all dates the restaurant is open"""
        dates = []
        for day in self.opening_hours:
            if self.opening_hours[day][1] > self.opening_hours[day][0]:
                dates.append(day)
        return dates

    def avg_open_hours_week(self) -> float:
        """
        Returns the average number of open hours per week, using all dates in the opening_hours dict dividing
        by 7 and rounding up to the nearest integer to get number of weeks
        TODO: Make it so the number of weeks is dependent on the dates and not just the number of days
        """
        total = timedelta()
        for day in self.opening_hours:
            opening_time, closing_time = self.get_opening_hours_date(day)
            total += closing_time - opening_time
        number_of_weeks = ceil(len(self.opening_hours) / 7)
        total_hours = total.total_seconds() / 3600
        return total_hours/number_of_weeks

    def avg_orders_per_day(self) -> float:
        """Returns the average number of orders per open day"""
        total_orders = len(self.orders_list)
        total_days = len(self.get_open_dates())
        return total_orders/total_days
