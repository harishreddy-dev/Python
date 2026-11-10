# 5-4. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
#                       if elif else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points. 
# • Write three versions of this program, making sure each message is printed
#   for the appropriate color alien.

alien_color = 'green'

# version 1
if alien_color == 'green':
    print("Hey, you earned 5 points...")
elif alien_color == 'yellow':
    print("Hey, you earned 10 points...")
else:
    print("Hey, you earned 15 points...")


alien_color = 'yellow'

# version 2
if alien_color == 'green':
    print("Hey, you earned 5 points...")
elif alien_color == 'yellow':
    print("Hey, you earned 10 points...")
else:
    print("Hey, you earned 15 points...")


alien_color = 'red'

# version 3
if alien_color == 'green':
    print("Hey, you earned 5 points...")
elif alien_color == 'yellow':
    print("Hey, you earned 10 points...")
else:
    print("Hey, you earned 15 points...")