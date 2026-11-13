# 6-6. Polling: Use the code in favorite_languages.py.
# • Make a list of people who should take the favorite languages poll. 
#   Include some names that are already in the dictionary and some that 
#   are not. 
# • Loop through the list of people who should take the poll. If they have
#   already taken the poll, print a message thanking them for responding.
#   If they have not yet taken the poll, print a message inviting them to
#   take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python', 
}

people = ['jen','ron','alex','sarah','tony','phil'] 

for person in people:
    if person in favorite_languages.keys():
        print(f"Hey {person.title()}, Thank you for responding.")
    else:
        print(f"Hey {person.title()}, you are invited to take the poll.")
