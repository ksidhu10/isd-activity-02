"""
Description: Unit tests for the Automobile class.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_automobile.py
"""
import unittest
from vehicle.automobile import Automobile

class TestAutomobile(unittest.TestCase):
    def test_init_attributes(self):
        auto = Automobile("Toyota", "Camry", 15, color="red")
        self.assertEqual(auto.make, "Toyota")
        self.assertEqual(auto.model, "Camry")
        self.assertEqual(auto.kilometers_per_litre, 15)

    def test_init_make_blank(self):
        with self.assertRaises(ValueError):
            Automobile("", "Camry", 15)

    def test_init_model_blank(self):
        with self.assertRaises(ValueError):
            Automobile("Toyota", "", 15)

    def test_init_kilometers_per_litre_non_numeric(self):
        with self.assertRaises(ValueError):
            Automobile("Toyota", "Camry", "fifteen")

    def test_str(self):
        auto = Automobile("Toyota", "Camry", 15)
        self.assertEqual(str(auto), "Automobile: Toyota Camry, Fuel Efficiency: 15 km/l")

    def test_calculate_fuel_requirements(self):
        auto = Automobile("Toyota", "Camry", 15)
        self.assertEqual(auto.calculate_fuel_requirements(300), 20)

if __name__ == "__main__":
    unittest.main()
