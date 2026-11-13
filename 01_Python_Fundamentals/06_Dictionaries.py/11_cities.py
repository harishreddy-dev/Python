# 6-11. Cities: Make a dictionary called cities. Use the names of three 
#               cities as keys in your dictionary. Create a dictionary 
#               of information about each city and include the country 
#               that the city is in, its approximate population, and one
#               fact about that city. The keys for each city’s dictionary
#               should be something like country, population, and fact. 
#               Print the name of each city and all of the information 
#               you have stored about it.

citites = {
    'Tokyo': {'country' : 'Japan', 'population' : '14 million', 'fact' : 'Technology'},
    'London': {'country' : 'United Kingdom', 'population' : '9 million', 'fact' : 'History'},
    'Melbourne':  {'country' : 'Australia', 'population' : '5 million', 'fact' : 'Education'}
}

for city, city_details in citites.items():
    print(f"{city.title()}, Details are:")
    for detail, info in city_details.items():
        print(f"{detail} is {info}")
    print("\n")
        
