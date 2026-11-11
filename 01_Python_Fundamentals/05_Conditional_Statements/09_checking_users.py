# 5-9. Checking Usernames: Do the following to create a program that si-
#                          -mulates how websites ensure that everyone has
#                          a unique username.
# • Make a list of five or more usernames called current_users. 
# • Make another list of five usernames called new_users. Make sure one 
#   or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has alr-
#   -eady been used. If it has, print a message that the person will need
#   to enter a new username. If a username has not been used, print a m-
#   -essage saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been u-
#   -sed,'JOHN' should not be accepted.

current_users = ['neha','harish','rahul','karthika','varun']

new_users = ['Ramu','Harish','Neha','Balu','Sachin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("user already exits, enter new username.")
    else:
        print("username is available")