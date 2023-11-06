# Q4. Write a Python program to iterate through both the keys and values of a dictionary and print them.

my_dict = {
    "Name": "Zainab Naeema",
    "Age": 18,
    "Location": "Ajman",
    "Occupation": "Student"}

for key, value in my_dict.items():
    print(f"{key}: {value}")
