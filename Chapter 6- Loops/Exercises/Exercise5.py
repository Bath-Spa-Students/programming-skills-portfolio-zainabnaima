# Exercise 5: No Pastrami

sandwich_orders = ["grilled cheese","pastrami", "nutella","pastrami", "vegetable", "pastrami", "chicken", "egg"]
finished_sandwiches = []

print("Apologies, we have run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I have prepared your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
