# Exercise 4: Rivers

Rivers = {'Nile': 'Egypt',
          'Amazon': 'Brazil',
          'Mississippi': 'United States'}

# Print sentences describing each river and the country it flows through
for River, Country in Rivers.items():
    print(f"The {River} River flows through {Country}.")

# Print the names of each river
print("\nRiver Names:")
for River in Rivers.keys():
    print(River)

# Print the names of each country
print("\nCountry Names:")
for Country in Rivers.values():
    print(Country)
