# 6.1 Person
user = {
    "first_name": "Renan",
    "last_name": "Nunes Steinck",
    "age": 24,
    "city": "Lages",
}

# 6.2 Favorite Numbers
favorite_numbers = {"renan": 42, "joci": 11, "waldir": 7, "erick": 8}


def print_favorite_number(fav_nums, name):
    print("{}'s favorite number is: {}".format(name.title(), fav_nums[name]))


print_favorite_number(favorite_numbers, "renan")
print_favorite_number(favorite_numbers, "joci")
print_favorite_number(favorite_numbers, "waldir")
print_favorite_number(favorite_numbers, "erick")

# 6.3 Glossary

programming_glossary = {
    "conditionals": "conditionals are reserved words that allows programs to run through different \
    routes based on inputs and conditions",
    "loops": "loops are reserved words that allow to have routes that repeat until a certain condition",
}

print(programming_glossary["conditionals"])
print(programming_glossary["loops"])

# 6.4 Glossary 2
for key, value in programming_glossary.items():
    print("\n", key.title())
    print("Definition: {}".format(value))

# 6.5 Rivers
rivers = {"nile": "egipt", "amazonas": "brazil", "itaipu": "paraguay/brazil"}

print("those are the rivers:")
for river in rivers.keys():
    print(river.title())

print("those are the places they are located:")
for located_in in rivers.values():
    print(located_in.title())

for k, v in rivers.items():
    print("{} is located in {}".format(k.title(), v.title()))

# 6.6 Pool
user_fav_langs = {
    "renan": ["Python"],
    "lucas": ["Python", "C#", "Typescript"],
    "jeferson": ["Typescript"],
    "enedir": ["Java", "C#"],
    "hugo": ["C#"],
}

user_answers = ["renan", "jeferson", "hugo"]

for user in user_fav_langs.keys():
    if user in user_answers:
        print("Thank you {} for your answer!".format(user.title()))
    else:
        print(
            "Hey {}, you haven't answered our pool yet, don't forget about it huh!".format(
                user.title()
            )
        )


people = [
    {"first_name": "Renan", "last_name": "Nunes Steinck", "age": 24, "city": "Lages",},
    {"first_name": "Jeferson", "last_name": "Costa", "age": 24, "city": "Taquari",},
    {"first_name": "Renan", "last_name": "Zapaloso", "age": 28, "city": "São Joaquim",},
]

for person in people:
    print("Let me tell you what I know about {}".format(person["first_name"]))
    print("Let me see... I know that his last name is {}".format(person["last_name"]))
    print("I know his age, he is {}".format(person["age"]))
    print("And I know that this person is from {}".format(person["city"]))
print("For now, that is all hahaha.")

# 6.7 Pets
# Create an array of dictonaries
pets = [
    {"name": "Aragog", "owner": {"name": "Renan",}, "race": "cat"},
    {"name": "Matilda", "owner": {"name": "Masha",}, "race": "cat"},
]

for pet in pets:
    print("Let me tell what I know about {}".format(pet["name"]))
    print("Let me see... I know that the owner is {}".format(pet["owner"]["name"]))
    print("ohhhhhh, and he/she is a {}".format(pet["race"]))

# 6.10 Favorite Numbers pt 2
favorite_numbers = {
    "renan": [42, 7, 14],
    "joci": [11, 2, 3],
    "waldir": [7, 11, 9],
    "erick": [8, 88, 23],
}

for key, value in favorite_numbers.items():
    print(
        "{} favorite numbers are: {}".format(
            key.capitalize(), ", ".join(map(str, value))
        )
    )
