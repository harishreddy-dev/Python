# 6-8. Pets: Make several dictionaries, where each dictionary represents
#            a different pet. In each dictionary, include the kind of a-
#            -nimal and the owner’s name. Store these dictionaries in a 
#            list called pets. Next, loop through your list and as you do
#            print everything you know about each pet.

pet_01 = {
    'animal type' : 'dog',
    'animal name' : 'tommy',
    'animal gender' : 'male',
    'animal onwner_name' : 'jensun'
}
pet_02 ={
    'animal type' : 'cat',
    'animal name' : 'norris',
    'animal gender' : 'female',
    'animal onwner_name' : 'belly'
}
pet_03 = {
    'animal type' : 'horse',
    'animal name' : 'bean',
    'animal gender' : 'male',
    'animal onwner_name' : 'harword'
}

pets = [pet_01, pet_02, pet_03]

for pet in pets:
    for detail, pet_info in pet.items():
        print(f"{detail.title()} is {pet_info.title()}")
    print("\n")