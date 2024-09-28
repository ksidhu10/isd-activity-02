"""
Description: Unit tests for the Aircrat class.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_aircraft.py
"""
import unittest
from vehicle.aircraft import Aircraft

class TestAircraft(unittest.TestCase):
    def test_init_attributes(self):
        aircraft = Aircraft("Boeing", "737", 2000, 800, color="white")
        self.assertEqual(aircraft.make, "Boeing")
        self.assertEqual(aircraft.model, "737")
        self.assertEqual(aircraft.fuel_burn_rate, 2000)
        self.assertEqual(aircraft.speed, 800)

    def test_init_make_blank(self):
        with self.assertRaises(ValueError):
            Aircraft("", "737", 2000, 800)

    def test_init_model_blank(self):
        with self.assertRaises(ValueError):
            Aircraft("Boeing", "", 2000, 800)

    def test_init_fuel_burn_rate_non_numeric(self):
        with self.assertRaises(ValueError):
            Aircraft("Boeing", "737", "two_thousand", 800)

    def test_init_speed_non_numeric(self):
        with self.assertRaises(ValueError):
            Aircraft("Boeing", "737", 2000, "eight_hundred")

    def test_str(self):
        aircraft = Aircraft("Boeing", "737", 2000, 800)
        self.assertEqual(str(aircraft), "Aircraft: Boeing 737, Speed: 800 km/h")

    def test_calculate_fuel_requirements(self):
        aircraft = Aircraft("Boeing", "737", 2000, 800)
        self.assertEqual(aircraft.calculate_fuel_requirements(2000), 4000)

if __name__ == "__main__":
    unittest.main()
