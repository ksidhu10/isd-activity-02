""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by:  Kiranjeet Kaur Sidhu
Date: 27-09-2024
"""

# Importing Shape classes
from shape import Triangle, Rectangle

# Importing Vehicle classes
from vehicle import Automobile, Aircraft, Train

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")
    # 1. Create an empty list of Shape objects.

    shapes = []
    # 2. Code a statement which creates an instance of the Triangle class.
    # Append the Triangle to the list of shapes.
    shapes.append(Triangle(11, 6, 7, 9, 11))

    # 3. Code a statement which creates an instance of the Rectangle class.
    # Append the Rectangle to the list of shapes.
    shapes.append(Rectangle(9, 4))

    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    shapes.append(Triangle(10, 5, 6, 8, 10))
    shapes.append(Rectangle(10, 5))
    shapes.append(Triangle(12, 6, 7, 9, 11))
    shapes.append(Rectangle(8, 4))
    shapes.append(Triangle(8, 4, 5, 6, 7))

    # 5. Iterate through the list of shapes.  On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")


# Add triangles and rectangles



    # *** END PART 1 ***

    # *** PART 2 ***
    print("*************PART 2****************")
    # 1. Create an empty list of Vehicle objects.
    vehicles = []

    # 2. Code a statement which creates an instance of the Automobile class.
    # Append the Automobile to the list of vehicles.
    vehicles.append(Automobile("Ford", "Escape", 11.0))

    # 3. Code a statement which creates an instance of the Aircraft class.
    # Append the Aircraft to the list of vehicles.
    vehicles.append(Aircraft("Boeing", "Airbus", 35.0, 540.0))

    # 4. Code 3 additional statements which creates an instance of 
    # Automobile, Aircraft or Train classes (your choice).
    # Append these instances to the list of vehicles.
    vehicles.append(Automobile("Ford", "Escape", 12.0))
    vehicles.append(Aircraft("Boeing", "Airbus", 40.0, 550.0))
    vehicles.append(Train("Siemens", "Intercity", 13, 0.03))
    vehicles.append(Automobile("Toyota", "Corolla", 15.0))
    vehicles.append(Aircraft("Airbus", "A380", 45.0, 600.0))

    # 5. Iterate through the list of vehicles.  On each iteration:
    # - print the vehicle
    # - print the phrase:
    # "Fuel needed for 500 kilometers: {fuel requirements} litres."
    for vehicle in vehicles:
        print(vehicle)
        try:
            print(f"Fuel needed for 500 kilometers: {vehicle.calculate_fuel_requirements(500):.2f} litres.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()