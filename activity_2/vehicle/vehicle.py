""""
Description: A class to represent generic Vehicle objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}"
    
    def calculate_fuel_requirements(self, distance):
        raise NotImplementedError("Subclass must implement this method")
