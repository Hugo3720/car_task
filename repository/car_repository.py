from models.car import Car, CarParseError


class CarRepository:
    def __init__(self):
        self._cars = []

    def add_from_strings(self, data_list):
        for data in data_list:
            try:
                car = Car.from_string(data)
                self._cars.append(car)
            except CarParseError as e:
                print(f"Ошибка: {data} -> {e}")

    def get_all(self):
        return list(self._cars)

    def find_by_number(self, number):
        return [c for c in self._cars if c.number == number]

    def filter_by_month(self, year, month):
        return sorted(
            [c for c in self._cars if c.date.year == year and c.date.month == month],
            key=lambda c: c.date
        )

    def filter_by_month(self, year, month):
        return sorted(
            [c for c in self._cars if c.date.year == year and c.date.month == month],
            key=lambda c: c.date
        )