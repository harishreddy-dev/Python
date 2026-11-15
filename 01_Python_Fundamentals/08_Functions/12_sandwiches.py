# 8-12. Sandwiches: Write a function that accepts a list of items a per-
#                   -son wants on a sandwich. The function should have 
#                   one parameter that collects as many items as the fu-
#                   -nction call provides, and it should print a summary
#                   of the sandwich that’s being ordered. Call the func-
#                   -tion three times, using a different number of argu-
#                   -ments each time.

def make_sandwich(*toppings):
    """"""
    print("The Selected Toppings on Sandwich:")
    for topping in toppings:
        print(topping)

make_sandwich('cheese','avocado','chilly flakes')
print("_________________________________________________________________")
make_sandwich('chicken','cheese')
print("_________________________________________________________________")
make_sandwich('egg')