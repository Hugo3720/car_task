"""Tests for car parser."""

from datetime import datetime

import pytest

from models.car import Car, CarParseError


def test_valid_car_parsing():
    data = "A123BC77 2023.05.10"

    car = Car.from_string(data)

    assert car.number == "A123BC77"
    assert car.date == datetime(2023, 5, 10)


def test_missing_number():
    data = "2023.05.10"

    with pytest.raises(CarParseError, match="Не найден номер"):
        Car.from_string(data)


def test_missing_date():
    data = "A123BC77"

    with pytest.raises(CarParseError, match="Не найдена дата"):
        Car.from_string(data)


def test_invalid_date():
    data = "A123BC77 2023.15.10"

    with pytest.raises(CarParseError, match="Некорректная дата"):
        Car.from_string(data)


def test_invalid_date2():
    data = "A123BC77 2023.02.29"

    with pytest.raises(CarParseError, match="Некорректная дата"):
        Car.from_string(data)


def test_str_method():
    car = Car("A123BC77", datetime(2023, 5, 10))

    assert str(car) == "A123BC77 2023.05.10"
