# 6-7. People: Start with the program you wrote for Exercise 6-1. Make two
#              new dictionaries representing different people, and store
#              all three dictionaries in a list called people. Loop thr-
#              -ough your list of people. As you loop through the list, 
#              print everything you know about each person.

person_01 = {
    'first_name' : 'David',
    'last_name' : 'Short',
    'age' : 19,
    'city' : 'New York'
}
person_02 = {
    'first_name' : 'Mark',
    'last_name' : 'Harword',
    'age' : 49,
    'city' : 'Austin'
}
person_03 = {
    'first_name' : 'Ronold',
    'last_name' : 'Jacking',
    'age' : 29,
    'city' : 'Texes'
}

people = [person_01, person_02, person_03]

for person in people:
    for detail, person_info in person.items():
        print(f"{detail.title()} is {person_info}")
    print("\n")