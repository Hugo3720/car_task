import unittest
from repository.car_repository import CarRepository


class TestRepo(unittest.TestCase):

    def setUp(self):
        self.repo = CarRepository()
        self.repo.add_from_strings([
            '"A1" 2023.05.10',
            '"A2" 2023.05.11'
        ])

    def test_find(self):
        self.assertEqual(len(self.repo.find_by_number("A1")), 1)