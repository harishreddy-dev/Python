# 3-7. Shrinking Guest List: You just found out that your new dinner ta-
#                            -ble won’t arrive in time for the dinner,a-
#                            -nd now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prin-
#   -ts a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
#   names remain in your list. Each time you pop a name from your list, 
#   print a message to that person letting them know you’re sorry you c-
#   -an’t invite them to dinner.
# • Print a message to each of the two people still on your list, letti-
#   -ng them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an 
#   empty list. Print your list to make sure you actually have an empty 
#   list at the end of your program.

print("Dinner Party")
guests = ['Harry Potter','Ronold Weasly','Hermione Granger']
print(f"Hey, {guests[0]} can you come home for Dinner...")
print(f"Hey, {guests[1]} can you come home for Dinner...")
print(f"Hey, {guests[2]} can you come home for Dinner...")
print(f"Oh!, Hermione Granger said she is unable to come to dinner...")
guests.remove('Hermione Granger')
guests.append('Prof.Snape')
print(f"Hey, {guests[2]} can you come home for Dinner...")
print("Hey, Guys i found a bigger table.")
guests.insert(0,'Draco Malfoy')
guests.insert(2,'Fred Weasly')
guests.append('Tom Riddle')
print(f"Hey, {guests[0]} can you come home for Dinner...")
print(f"Hey, {guests[1]} can you come home for Dinner...")
print(f"Hey, {guests[2]} can you come home for Dinner...")
print(f"Hey, {guests[3]} can you come home for Dinner...")
print(f"Hey, {guests[4]} can you come home for Dinner...")
print(f"Hey, {guests[5]} can you come home for Dinner...")

print("Hey, Sorry Everyone the new dinner table can't arrive in time.")
print("I can only invite 2 people only...")
deleted_guest = guests.pop()
print(f"Sorry {deleted_guest}, your dinner invitation is canceled.")
deleted_guest = guests.pop()
print(f"Sorry {deleted_guest}, your dinner invitation is canceled.")
deleted_guest = guests.pop()
print(f"Sorry {deleted_guest}, your dinner invitation is canceled.")
deleted_guest = guests.pop()
print(f"Sorry {deleted_guest}, your dinner invitation is canceled.")
print("----------------------------------------------------------------------")
print(f"Hey, {guests[0]} you are still invited to dinner.")
print(f"Hey, {guests[1]} you are still invited to dinner.")
print("----------------------------------------------------------------------")

del guests[0:]

print(guests)