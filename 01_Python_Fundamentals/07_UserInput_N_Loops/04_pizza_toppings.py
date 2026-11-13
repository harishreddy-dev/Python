# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a se-
#                      -ries of pizza toppings until they enter a 'quit'
#                      value. As they enter each topping, print a message
#                      saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter your toppings: ").lower()
    if topping == 'quit':
        break
    else:
        print(f"{topping} will be added to your pizza...")