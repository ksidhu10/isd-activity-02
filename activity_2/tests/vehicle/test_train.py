"""
Description: Unit tests for the Train class.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_train.py
"""
import unittest
from vehicle.train import Train

class TestTrain(unittest.TestCase):
    def test_init_attributes(self):
        train = Train("Amtrak", "Express", 8, 3.0, color="blue")
        self.assertEqual(train.make, "Amtrak")
        self.assertEqual(train.model, "Express")
        self.assertEqual(train.cars, 8)
        self.assertEqual(train.base_fuel_rate, 3.0)

    def test_init_make_blank(self):
        with self.assertRaises(ValueError):
            Train("", "Express", 8, 3.0)

    def test_init_model_blank(self):
        with self.assertRaises(ValueError):
            Train("Amtrak", "", 8, 3.0)

    def test_init_cars_not_integer(self):
        with self.assertRaises(ValueError):
            Train("Amtrak", "Express", "eight", 3.0)

    def test_init_base_fuel_rate_non_numeric(self):
        with self.assertRaises(ValueError):
            Train("Amtrak", "Express", 8, "three")

    def test_str(self):
        train = Train("Amtrak", "Express", 8, 3.0)
        self.assertEqual(str(train), "Train: Amtrak Express, Cars: 8, Base Fuel Rate: 3.0")

    def test_calculate_fuel_requirements(self):
        train = Train("Amtrak", "Express", 8, 3.0)
        self.assertEqual(train.calculate_fuel_requirements(500), 1500)

if __name__ == "__main__":
    unittest.main()
