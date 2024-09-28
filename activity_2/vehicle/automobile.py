""""
Description: A class to represent Automobile objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
from vehicle import Vehicle

class Automobile(Vehicle):

    def __init__(self, make, model, kilometers_per_litre):
        super().__init__(make, model)
        if not isinstance(kilometers_per_litre, (int, float)):
            raise ValueError("Kilometers per litre must be numeric.")
        self.kilometers_per_litre = kilometers_per_litre
    
    def __str__(self):
        return super().__str__() + f"\nThis automobile can drive {self.kilometers_per_litre} kilometers per litre."
    
    def calculate_fuel_requirements(self, distance):
        return distance / self.kilometers_per_litre
