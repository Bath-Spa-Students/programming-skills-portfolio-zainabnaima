''' Q4. Assume the lists numbers1 has 100 elements and numbers2 is 
an empty list. Write code that copies the values in numbers to numbers2.'''

# Create a list with 100 elements
numbers1 = [i for i in range(1, 101)]
# Create an empty list
numbers2 = []

# Copy values from numbers1 to numbers2
for num in numbers1:
    numbers2.append(num)

# Now, numbers2 contains the same elements as numbers1
print(numbers2)
