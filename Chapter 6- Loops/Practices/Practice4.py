''' Q4. Write a Python program that uses the break statement to exit a for loop 
when a specific condition is met'''

for num in range(5,100,5):
    if num == 55:
        break
    print(num)
