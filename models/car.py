import re
from datetime import datetime


class CarParseError(Exception):
    pass


class Car:
    def __init__(self, number: str, date: datetime):
        self.number = number
        self.date = date

    @classmethod
    def from_string(cls, data: str):
        number_match = re.findall(r'"(.*?)"', data)
        date_match = re.findall(r'\d{4}\.\d{2}\.\d{2}', data)

        if not number_match:
            raise CarParseError("Не найден номер")

        if not date_match:
            raise CarParseError("Не найдена дата")

        try:
            date = datetime.strptime(date_match[0], "%Y.%m.%d")
        except ValueError:
            raise CarParseError("Некорректная дата")

        return cls(number_match[0], date)

    def __str__(self):
        return f"{self.number} {self.date.strftime('%Y.%m.%d')}"