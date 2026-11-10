# 3-5. Changing Guest List: You just heard that one of your guests can’t
#                           make the dinner, so you need to send out new
#                           set of invitations. You’ll have to think of 
#                           someone else to invite.

guests = ['Harry Potter','Ronold Weasly','Hermione Granger']
print(f"Hey, {guests[0]} can you come home for Dinner...")
print(f"Hey, {guests[1]} can you come home for Dinner...")
print(f"Hey, {guests[2]} can you come home for Dinner...")
print(f"Oh!, Hermione Granger said she is unable to come to dinner...")
guests.remove('Hermione Granger')
guests.append('Prof.Snape')
print(f"Hey, {guests[2]} can you come home for Dinner...")