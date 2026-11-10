# 5-3. Alien Colors #2: Choose a color for an alien as you did in Exerc-
#                       -ise 5-2, and write an if-else chain.
# • If the alien’s color is green,print a statement that the player just
#   earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player 
#   just earned 10 points.
# • Write one version of this program that runs the if block and another
#   that runs the else block.

alien_colour = 'green'

# if version
if alien_colour == 'green':
    print("Hey, you earned 5 points...")
else:
    print("Hey, you earned 10 points...")

alien_colour = 'yellow'

# else version
if alien_colour == 'green':
    print("Hey, you earned 5 points...")
else:
    print("Hey, you earned 10 points...")