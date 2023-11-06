''' Q5. Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

largest = None
while True:
    user_input = input("Enter a number (or '0' to exit): ")
    if user_input == '0':
        break
    num = int(user_input)
    if largest is None or num > largest:
        largest = num

print("The largest number entered is:", largest)
