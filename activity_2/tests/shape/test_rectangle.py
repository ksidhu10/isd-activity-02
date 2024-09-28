"""
Description: Unit tests for the Rectangle class.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_rectangle.py
"""

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init_attributes(self):
        rectangle = Rectangle(10, 5, color="blue")
        self.assertEqual(rectangle.length, 10)
        self.assertEqual(rectangle.width, 5)

    def test_init_color_blank(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, color="")

    def test_init_length_not_integer(self):
        with self.assertRaises(ValueError):
            Rectangle("ten", 5)

    def test_init_width_not_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(10, "five")

    def test_str(self):
        rectangle = Rectangle(10, 5, color="blue")
        self.assertEqual(str(rectangle), "Rectangle with length 10, width 5")

    def test_calculate_area(self):
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.calculate_area(), 50)

    def test_calculate_perimeter(self):
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.calculate_perimeter(), 30)

if __name__ == "__main__":
    unittest.main()
