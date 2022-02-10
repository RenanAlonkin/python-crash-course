# 5.3 Alien colors #1
# Write a variable called alien_color and assign a value
# it can be 'green', 'yellow' or 'red'.


def test_alien_color(alien_color):
    # Write an if condition to test if it is green
    if alien_color.lower() == "green":
        print("Congrats, you just won 5 points")


# Success example test
alien_color = "green"
test_alien_color(alien_color)

# Failure example test
alien_color = "yellow"
test_alien_color(alien_color)


# 5.4 Alien colors #2
# Write down a if else example


def test_alien_color(alien_color):
    if alien_color.lower() == "green":
        print("Congrats, you just won 5 points")
    else:
        print("Congrats, you just won 10 points")


# Success example test
alien_color = "green"
test_alien_color(alien_color)

# Failure example test
alien_color = "yellow"
test_alien_color(alien_color)

# 5.5 Alien colors #3
# Write down a if elif else test


def test_alien_color(alien_color):
    alien_color = alien_color.lower()
    # Write an if condition to test if it is green
    if alien_color == "green":
        print("Congrats, you just won 5 points")
    elif alien_color == "yellow":
        print("Congrats, you just won 10 points")
    elif alien_color == "red":
        print("Congrats, you just won 15 points")


alien_color = "green"
test_alien_color(alien_color)

alien_color = "yellow"
test_alien_color(alien_color)

alien_color = "red"
test_alien_color(alien_color)

# 5.6 Life Stages
# Define a variable age and:
age = 24


def print_life_stage(age):
    # Baby
    if age < 2:
        print("You are a baby!")
    elif age < 4:
        print("You are a child!")
    elif age < 13:
        print("You are a kid")
    elif age < 20:
        print("You are a teenager")
    elif age < 65:
        print("You are an adult")
    else:
        print("you are an elder")


print_life_stage(age)

# 5.7 Favorite Frut
# create a list of your favorite fruits, and, then,
# write a serie of independent ifs. If the fruit is in
# your favorite fruits list write a phrase

my_favorite_fruits = ["kiwi", "maracuja", "strawberry", "grapes"]

if "kiwi" in my_favorite_fruits:
    print("Great choice!")

if "maracuja" in my_favorite_fruits:
    print("Maracuja then? hummmm, interesting, me too!")

if "strawberry" in my_favorite_fruits:
    print("Oh, okay, it is starting to be scary, we have the same taste")

if "grapes" in my_favorite_fruits:
    print("You have such a great taste!")
