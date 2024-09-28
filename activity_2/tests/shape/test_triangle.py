"""
Description: Unit tests for the Book class.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_init_attributes(self):
        triangle = Triangle(3, 4, 5, color="green")
        self.assertEqual(triangle.side_1, 3)
        self.assertEqual(triangle.side_2, 4)
        self.assertEqual(triangle.side_3, 5)

    def test_init_color_blank(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, 5, color="")

    def test_init_side1_not_integer(self):
        with self.assertRaises(ValueError):
            Triangle("three", 4, 5)

    def test_init_side2_not_integer(self):
        with self.assertRaises(ValueError):
            Triangle(3, "four", 5)

    def test_init_side3_not_integer(self):
        with self.assertRaises(ValueError):
            Triangle(3, 4, "five")

    def test_str(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(str(triangle), "Triangle with sides 3, 4, 5")

    def test_calculate_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0)

    def test_calculate_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.calculate_perimeter(), 12)

if __name__ == "__main__":
    unittest.main()
