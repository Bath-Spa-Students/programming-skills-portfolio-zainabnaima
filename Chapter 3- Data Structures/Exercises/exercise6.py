# Exercise 6: Shrinking Guest List
guests = ["Hameema", "Asbeena", "Noora","Afsheena","Noha"]
message = "Dear {}, you are invited to dinner at my place!"

print("I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry, {}, I can't invite you to dinner.".format(removed_guest))

for guest in guests:
    print(message.format(guest))

# Empty the list
del guests[:]
print("Guest list is now empty:", guests)
