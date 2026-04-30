"""Repository for parsed car records."""

from models.car import Car, CarParseError


class CarRepository:
    """Stores cars and provides search/filter operations."""

    def __init__(self) -> None:
        self._cars: list[Car] = []
        self._errors: list[str] = []

    def add_from_strings(self, data_list: list[str]) -> list[str]:
        """Parse source strings, store valid cars, and return parse errors."""
        self._errors.clear()

        for data in data_list:
            try:
                self._cars.append(Car.from_string(data))
            except CarParseError as exc:
                self._errors.append(f"Ошибка: {data} -> {exc}")

        return list(self._errors)

    def get_all(self) -> list[Car]:
        """Return all stored cars."""
        return list(self._cars)

    def get_errors(self) -> list[str]:
        """Return errors from the latest import operation."""
        return list(self._errors)

    def find_by_number(self, number: str) -> list[Car]:
        """Find cars with the exact registration number."""
        return [car for car in self._cars if car.number == number]

    def filter_by_month(self, year: int, month: int) -> list[Car]:
        """Return cars for the selected month sorted by date."""
        return sorted(
            [
                car
                for car in self._cars
                if car.date.year == year and car.date.month == month
            ],
            key=lambda car: car.date,
        )
