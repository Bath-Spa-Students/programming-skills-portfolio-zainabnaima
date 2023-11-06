# if-else statement
# Get the user's age integer input.
age = int(input("Enter Your Age: "))
if age >= 18:
    print('You are major')
else:
    print('You are minor')


# nested if-else statement
# Define two variables
x = 210
y = 50
# Check if x is greater than 5
if x > 5:
    print("x is greater than 5")
    if y < 2:
        print("y is less than 2")
    else:
        # If y is not less than 2, print this message
        print("y is not less than 2")
else:
    # If x is not greater than 5, print this message
    print("x is not greater than 5")


# if-elif-else statement
# Get the user's income as input
income = float(input('Enter your salary: '))
# Check income range and provide a message
if income < 20000:
    print('Your income is low.')
elif 20000 <= income < 50000:
    print('Your income is moderate.')
elif 50000 <= income < 100000:
    print('Your income is high.')
else:
    print('Your income is very high.')



