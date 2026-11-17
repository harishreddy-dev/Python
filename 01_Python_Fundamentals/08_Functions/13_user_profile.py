# 8-13. User Profile: Start with a copy of user_profile.py. Build a pro-
#                     -file of yourself by calling build_profile(), using   
#                     your first and last names and three other key-value
#                     pairs that describe you.

# user_profile.py
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything known about a user.""" 
    user_info['first_name'] = first
    user_info['last_name'] = last 
    return user_info

user_profile = build_profile('Harish','Reddy', gender='Male', age=19,
                             country='India')

print(user_profile)
