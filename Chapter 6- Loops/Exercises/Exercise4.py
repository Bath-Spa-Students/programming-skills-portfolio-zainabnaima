# Exercise 4: Deli

sandwich_orders = ["grilled cheese", "nutella", "vegetable", "chicken", "egg"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop(0)
    print(f"I have prepared your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
