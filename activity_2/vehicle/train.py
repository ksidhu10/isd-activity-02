""""
Description: A class to represent Train objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
from vehicle import Vehicle

class Train(Vehicle):

    def __init__(self, make, model, cars, base_fuel_rate):
        super().__init__(make, model)
        if not isinstance(cars, int):
            raise ValueError("Cars must be numeric.")
        if not isinstance(base_fuel_rate, (int, float)):
            raise ValueError("Base fuel rate must be numeric.")
        self.cars = cars
        self.base_fuel_rate = base_fuel_rate
    
    def __str__(self):
        return super().__str__() + f"\nThis train has a base fuel rate of {self.base_fuel_rate} litres/kilometer, and contains {self.cars} cars."
    
    def calculate_fuel_requirements(self, distance):
        total_fuel = self.base_fuel_rate * (1.1 * self.cars)
        return total_fuel * distance
