#! python3

from enum import Enum

class Weekday(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

    def __str__(self) -> str:
        return self.name


class Time():
    """Class to represent times during a day, has simple arithmetic operations and comparison operators"""
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes}"

    def __sub__(self, other):
        return Time(self.hours - other.hours, self.minutes - other.minutes)

    def __add__(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes)

    def __bool__(self) -> bool:
        if self.hours == 0 and self.minutes == 0:
            return False
        return True

    def __gt__(self, other) -> bool:
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.hours} hours and {self.minutes} minutes"