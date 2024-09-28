""""
Description: A class to represent Aircraft objects.
Author:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""
from vehicle import Vehicle

class Aircraft(Vehicle):

    def __init__(self, make, model, fuel_burn_rate, speed):
        super().__init__(make, model)
        if not isinstance(fuel_burn_rate, (int, float)):
            raise ValueError("Fuel burn rate must be numeric.")
        if not isinstance(speed, (int, float)):
            raise ValueError("Speed must be numeric.")
        self.fuel_burn_rate = fuel_burn_rate
        self.speed = speed
    
    def __str__(self):
        return super().__str__() + f"\nThis aircraft has a fuel burn rate of {self.fuel_burn_rate} litres/hour, and a cruising speed of {self.speed} km/hour."
    
    def calculate_fuel_requirements(self, distance):
        flight_time = distance / self.speed
        return flight_time * self.fuel_burn_rate
