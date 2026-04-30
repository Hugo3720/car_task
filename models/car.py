"""Car domain model and parser."""

from dataclasses import dataclass
from datetime import datetime
import re


CAR_NUMBER_PATTERN = re.compile(r"\b[АВЕКМНОРСТУХA-Z]\d{3}[АВЕКМНОРСТУХA-Z]{2}\d{2,3}\b")
DATE_PATTERN = re.compile(r"\d{4}\.\d{2}\.\d{2}")
DATE_FORMAT = "%Y.%m.%d"


class CarParseError(Exception):
    """Raised when a car record cannot be parsed."""


@dataclass(frozen=True, slots=True)
class Car:
    """Car record with registration number and date."""

    number: str
    date: datetime

    @classmethod
    def from_string(cls, data: str) -> "Car":
        """Parse a car from a string containing a number and YYYY.MM.DD date."""
        number_match = CAR_NUMBER_PATTERN.search(data)
        date_match = DATE_PATTERN.search(data)

        if number_match is None:
            raise CarParseError("Не найден номер")

        if date_match is None:
            raise CarParseError("Не найдена дата")

        try:
            date = datetime.strptime(date_match.group(), DATE_FORMAT)
        except ValueError as exc:
            raise CarParseError("Некорректная дата") from exc

        return cls(number_match.group(), date)

    def __str__(self) -> str:
        return f"{self.number} {self.date.strftime(DATE_FORMAT)}"
