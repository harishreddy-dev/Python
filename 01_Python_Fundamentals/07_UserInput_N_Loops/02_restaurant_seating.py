# 7-2. Restaurant Seating: Write a program that asks the user how many 
#                          people are in their dinner group. If the ans-
#                          -wer is more than eight, print a message say-
#                          -ing they’ll have to wait for a table. Other-
#                          -wise, report that their table is ready.

group = int(input("Hey, How many people are in your dinner group: "))

if 8 < group:
    print("Sorry, You have to wait for a table...")
else:
    print("Hey, your table is ready...")