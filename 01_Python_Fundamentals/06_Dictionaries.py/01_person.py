# 6-1. Person: Use a dictionary to store information about a person you 
#              know. Store their first name, last name, age, and the city
#              in which they live. You should have keys such as first_n-
#              -ame, last_name, age, and city. Print each piece of info-
#              -rmation stored in your dictionary.

person_details = {
    "first_name" : "David",
    "last_name" : "short",
    "age" : 19,
    "city" : "New York"
}

for person , detail in person_details.items():
    print(f"{person} is {detail}")

