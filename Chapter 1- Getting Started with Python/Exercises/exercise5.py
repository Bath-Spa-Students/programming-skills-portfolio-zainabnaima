radius_str = input("Enter the radius of the circle: ")
try:
    radius = float(radius_str)
    if radius < 0:
        print("Please enter a positive radius.")
    else:
        area = 3.14159 * radius * radius 
        print(f"The area of the circle with radius {radius} is {area:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")