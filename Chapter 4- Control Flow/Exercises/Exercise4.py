# Define the variable age and set its value to the person's age. 
# Change this value to determine the stage of life.

age = 25

# Check the person's age and print the corresponding life stage.
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    # If the person's age is 65 or older, they are considered an elder.
    print("The person is an elder.")
