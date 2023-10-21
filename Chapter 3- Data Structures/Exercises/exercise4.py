# Exercise 4: Guest List

guests = ["Hameema", "Asbeena", "Noora","Afsheena","Noha"]
message = "Dear {}, you are invited to dinner at my place!"

for guest in guests:
    print(message.format(guest))
