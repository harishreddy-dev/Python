# 6-9. Favorite Places: Make a dictionary called favorite_places. Think 
#                       of three names to use as keys in the dictionary,
#                       and store one to three favorite places for each 
#                       person. To make this exercise a bit more intere-
#                       -sting, ask some friends to name a few of their 
#                       favorite places. Loop through the dictionary, and
#                       print each person’s name and their favorite places.

favorite_places = {
    'harish' : ['hyderabad','new york','melbourne'],
    'sam' : ['mumbai','shimla',],
    'rahul' : ['bengaluru']
}
for person, places in favorite_places.items():
    print(f"{person.title()} Favorite places:")
    for place in places:
        print(f"\t{place.title()}")
    print("\n")