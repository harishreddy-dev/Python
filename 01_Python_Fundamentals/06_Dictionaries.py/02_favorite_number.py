# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite nu-
#                        -mbers. Think of five names, and use them as k-
#                        -eys in your dictionary. Think of a favorite n-
#                        -umber for each person, and store each as a va-
#                        -lue in your dictionary. Print each person’s name
#                        and their favorite number. For even more fun
#                        poll a few friends and get some actual data
#                        for your program.

favorite_numbers = {
    "Neha" : 6,
    "Reddy" : 1,
    "Harish" : 10,
    "Ramya" : 7,
    "Kiran" : 3
}

for person, number in favorite_numbers.items():
    print(f"{person}'s favorite number: {number}")
