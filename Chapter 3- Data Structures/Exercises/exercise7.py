# Exercise 7: Seeing the World
places_to_visit = ["Palestine", "Turkey", "Switzerland", "Saudi Arabia"]

print("Original order:")
print(places_to_visit)

print("\nAlphabetical order:")
print(sorted(places_to_visit))

print("\nOriginal order (still the same):")
print(places_to_visit)

print("\nReverse alphabetical order:")
print(sorted(places_to_visit, reverse=True))

print("\nOriginal order (still the same):")
print(places_to_visit)

print("\nReversed order:")
places_to_visit.reverse()
print(places_to_visit)

print("\nReversed order again (back to the original order):")
places_to_visit.reverse()
print(places_to_visit)

print("\nAlphabetical order:")
places_to_visit.sort()
print(places_to_visit)

print("\nReverse alphabetical order:")
places_to_visit.sort(reverse=True)
print(places_to_visit)
