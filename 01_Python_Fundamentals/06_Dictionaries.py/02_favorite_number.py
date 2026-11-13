# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite nu-
#                        -mbers. Think of five names, and use them as k-
#                        -eys in your dictionary. Think of a favorite n-
#                        -umber for each person, and store each as a va-
#                        -lue in your dictionary. Print each person’s name
#                        and their favorite number. For even more fun
#                        poll a few friends and get some actual data
#                        for your program.

favorite_numbers = {
    'Neha' : 6,
    'Reddy' : 1,
    'Harish' : 10,
    'Ramya' : 7,
    'Kiran' : 3
}

print(f"Neha favorite number: {favorite_numbers.get("Neha")}")
print(f"Reddy favorite number: {favorite_numbers.get("Reddy")}")
print(f"Harish favorite number: {favorite_numbers.get("Harish")}")
print(f"Ramya favorite number: {favorite_numbers.get("Ramya")}")
print(f"Kiran favorite number: {favorite_numbers.get("Kiran")}")
