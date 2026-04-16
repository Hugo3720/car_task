import pytest
from datetime import datetime

from repository.car_repository import CarRepository


@pytest.fixture
def repo():
    return CarRepository()


@pytest.fixture
def sample_data():
    return [
        "A123BC77 2023.05.10",
        "B456DE77 2023.05.15",
        "C789FG77 2023.06.01",
        "INVALID DATA",
        "D000HH77 2023.99.99",  # некорректная дата
        "C7899FG77 2023.06.01", # некорректный номер
    ]


def test_add_from_strings_valid_and_invalid(repo, sample_data):
    repo.add_from_strings(sample_data)

    cars = repo.get_all()

    # должно добавиться только 3 валидных объекта
    assert len(cars) == 3


def test_added_objects_content(repo):
    repo.add_from_strings(["A123BC77 2023.05.10"])

    car = repo.get_all()[0]
    print(car.__str__())

    assert car.number == "A123BC77"
    assert car.date == datetime(2023, 5, 10)


def test_find_by_number_found(repo):
    repo.add_from_strings([
        "A123BC77 2023.05.10",
        "A123BC77 2023.06.10",
        "B456DE77 2023.05.15",
    ])

    result = repo.find_by_number("A123BC77")

    assert len(result) == 2
    assert all(c.number == "A123BC77" for c in result)


def test_find_by_number_not_found(repo):
    repo.add_from_strings(["A123BC77 2023.05.10"])

    result = repo.find_by_number("ZZZ999")

    assert result == []


def test_filter_by_month(repo):
    repo.add_from_strings([
        "A123BC77 2023.05.20",
        "B456DE77 2023.05.10",
        "C789FG77 2023.06.01",
    ])

    result = repo.filter_by_month(2023, 5)

    assert len(result) == 2


def test_filter_by_month_sorted(repo):
    repo.add_from_strings([
        "A123BC77 2023.05.20",
        "B456DE77 2023.05.10",
        "C789FG77 2023.05.15",
    ])

    result = repo.filter_by_month(2023, 5)

    dates = [c.date for c in result]

    assert dates == sorted(dates)


def test_filter_by_month_empty(repo):
    repo.add_from_strings([
        "A123BC77 2023.06.01",
    ])

    result = repo.filter_by_month(2023, 5)

    assert result == []