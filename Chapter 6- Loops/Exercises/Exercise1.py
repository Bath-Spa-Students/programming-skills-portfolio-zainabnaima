# Exercise 1: Pizza Toppings 

pizza_toppings = []
while True:
    toppings = input("Enter a pizza topping (or 'quit' to finish): ")
    if toppings.lower() == 'quit':
        break
    print(f" I will add {toppings} to your pizza.")
    pizza_toppings.append(toppings)

print("\nToppings for your pizza:")
for toppings in pizza_toppings:
    print(toppings)
