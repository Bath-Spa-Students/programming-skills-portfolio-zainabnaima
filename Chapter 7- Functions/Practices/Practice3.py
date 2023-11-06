# Q3. Write a Python program that uses a function to check if a given number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

number = 557
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
