# Exercise 5: Pets

pets = [{'animal_type': 'Cat', 'owner_name': 'Niya'},
        {'animal_type': 'Rabbit', 'owner_name': 'Alisha'},
        {'animal_type': 'Hamster', 'owner_name': 'Nicole'}]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Type of Animal: {pet['animal_type']}")
    print(f"Owner's Name: {pet['owner_name']}")
    print()
