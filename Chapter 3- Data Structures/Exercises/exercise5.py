# Exercise 5: Change Guest List
guests = ["Hameema", "Asbeena", "Noora","Afsheena","Noha"]
message = "Dear {}, you are invited to dinner at my place!"

print("Unfortunately, {} can't make it.".format(guests[1]))

# Replace the guest who can't make it with a new guest
guests[1] = "Asmeera"

# Sending new invitations
for guest in guests:
    print(message.format(guest))
