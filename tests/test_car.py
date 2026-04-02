import unittest
from models.car import Car, CarParseError


class TestCar(unittest.TestCase):

    def test_valid(self):
        car = Car.from_string('"A123" 2023.05.10')
        self.assertEqual(car.number, "A123")

    def test_invalid(self):
        with self.assertRaises(CarParseError):
            Car.from_string('invalid')