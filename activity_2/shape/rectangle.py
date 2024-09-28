""""
Description: A class to represent Rectangle objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
from shape import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle with length {self.length}, width {self.width}"

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    
