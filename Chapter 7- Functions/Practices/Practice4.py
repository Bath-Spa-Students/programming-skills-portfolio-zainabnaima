''' Q4. Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius.'''

import math

def calculate_area(radius):
    return math.pi * radius ** 2

# Example usage:
radius = 5
area = calculate_area(radius)
print(f"Area of the circle with radius {radius} is {area:.2f}")
