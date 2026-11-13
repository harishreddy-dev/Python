# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make
#                   sure the sandwich 'pastrami' appears in the list at 
#                   least three times. Add code near the beginning of your
#                   program to print a message saying the deli has run out
#                   of pastrami, and then use a while loop to remove all
#                   occurrences of 'pastrami' from sandwich_orders. Make
#                   sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami sandwich','grill cheese sandwich',
                   'pastrami sandwich','chicken sandwich','veg sandwich',
                   'tuna sandwich','pastrami sandwich']

print("The Deli has run out of pastrami...")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami sandwich':
        finished_sandwiches.append(sandwich)


print("Listing each sandwich that was made: ")
for sandwich in reversed(finished_sandwiches):
    print(f"{sandwich.title()}")