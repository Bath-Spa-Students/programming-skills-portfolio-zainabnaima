'''Q3: Write a python program that takes an input 5 from user and 
then type cast those values to string, int and float in the separate
variables. Print all the variables.'''

# Input a number from the user
num = input("Enter a number: ")

# Typecast the input to int, float, and string
num_int = int(num)
num_float = float(num)
num_str = str(num)

# Print the variables
print(f"Integer: {num_int}")
print(f"Float: {num_float}")
print(f"String: {num_str}")
