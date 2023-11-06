# Q2. Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 7
result = factorial(n)
print(f"Factorial of {n} is {result}")
