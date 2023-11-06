# Q5. Write a Python program to merge two dictionaries into one.

# Define two dictionaries
dict1 = {"red": 1, "blue": 2}
dict2 = {"green": 3, "yellow": 4}

# Merge the two dictionaries into a new one
dict3 = {**dict1, **dict2}

# Print the merged dictionary
print(dict3)

