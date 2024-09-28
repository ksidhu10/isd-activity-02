""""
Description: A class to represent Triangle objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
import math
from shape import Shape

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        return f"Triangle with base {self.base}, height {self.height}"
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    
