# Exercise 2: Movie Tickets

while True:
    Age = input("Please enter your age (or 'quit' to finish): ")
    if Age.lower() == 'quit':
        break
    age = int(Age)
    if age < 3:
        print("Your ticket is free.")
    elif age>=3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
