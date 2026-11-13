# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each 
#                         person can have more than one favorite number.
#                         Then print each person’s name along with their
#                         favorite numbers.

favorite_numbers = {
    'Neha' : [6,9],
    'Reddy' : [1,7],
    'Harish' : [10,9],
    'Ramya' : [11,33],
    'Kiran' : [18,2]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()} favorite numbers :")
    for number in numbers:
        print(f"{number}")
    print("\n")
    