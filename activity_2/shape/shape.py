""""
Description: A class to represent generic Shape objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def calculate_perimeter(self):
        raise NotImplementedError("Subclass must implement this method")
    
    def __str__(self):
        return "Shape object"
