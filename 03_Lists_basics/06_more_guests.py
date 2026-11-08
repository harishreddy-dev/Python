# 3-6. More Guests: You just found a bigger dinner table, so now more s-
#                   -pace is available. Think of three more guests to i-
#                   -nvite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call
#  to the end of your program, informing people that you found a bigger 
#  table. 
# • Use insert() to add one new guest to the beginning of your list. 
# • Use insert() to add one new guest to the middle of your list. 
# • Use append() to add one new guest to the end of your list. 
# • Print a new set of invitation messages, one for each person in your 
#   list.

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