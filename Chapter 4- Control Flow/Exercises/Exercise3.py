# Define the variable alien_color and assign it a value.
# Change this value to test different outcomes.

# if block
alien_color = 'green'
# Check the color of the alien and provide points accordingly.
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    # If the alien's color is not green or yellow, the player earns 15 points.
    print("The player earned 15 points.")

# elif block
alien_color = 'yellow'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")
    
# else block
alien_color = 'red'
if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")
