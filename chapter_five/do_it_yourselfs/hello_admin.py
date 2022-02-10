# 5.8 Hello Admin
# Write down a greeting to the users

users = ["admin", "carlos", "vitor", "taise", "maju"]

if users:
    for user in users:
        if user == "admin":
            print("Welcome back admin, would you like to see a status report?")
        else:
            print("Hello there", user.title(), "nice to see you again!")

else:
    print("No user found, we need to register at least one user")

# Verify if new user is in current users
current_users = ["pedro", "viktor", "jona", "renan", "giorgi"]
new_users = ["pedro", "viktor", "maribel", "cesar"]

for new_user in new_users:
    is_avaliable = True
    print("Looking for", new_user)
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            is_avaliable = False
    if is_avaliable:
        print("Oh, great, this username looks to be avaliable!")
    else:
        print("Sorry, this username is already in use.")

# 5.11 Ordinal numbers
numbers = list(range(1, 10, 1))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print("{}th".format(number))
