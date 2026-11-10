# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
#                               Make a copy of the list of pizzas, and 
#                               call it friend_pizzas. Then, do the fol-
#                               -lowing:
# • Add a new pizza to the original list. 
# • Add a different pizza to the list friend_pizzas. 
# • Prove that you have two separate lists. Print the message My favori-
#   -te pizzas are:, and then use a for loop to print the first list. 
#   Print the message My friend’s favorite pizzas are:, and then use a 
#   for loop to print the second list. Make sure each new pizza is stored
#   in the appropriate list.

my_pizzas = ['cheese pizza','chicken pizza','corn pizza']
friend_pizzas = my_pizzas[:]

my_pizzas.append('mushroom pizza')
friend_pizzas.append('veg pizza')

print("My fav pizzas :")
for pizza in my_pizzas:
    print(pizza)
print("\n")
print("My friend fav pizzas :")
for pizza in friend_pizzas:
    print(pizza)