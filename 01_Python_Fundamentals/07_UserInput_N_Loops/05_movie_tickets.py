# 7-5. Movie Tickets: A movie theater charges different ticket prices 
#                     depending on a person’s age. If a person is under 
#                     the age of 3, the ticket is free; if they are bet-
#                     -ween 3 and 12, the ticket is $10; and if they are
#                     over age 12, the ticket is $15. Write a loop in w-
#                     -hich you ask users their age, and then tell them 
#                     the cost of their movie ticket.

while True:
    age = int(input("Enter your age: "))

    if age < 3:
        print("Hey, the ticket is free...")
    elif 3 <= age <= 12:
        print("Hey, the ticket is $10...")
    else:
        print("Hey, the ticket is $15...")


