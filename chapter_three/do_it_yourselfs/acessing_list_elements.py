# 3.1 Store the name of your friends
friend_names = ['Lucas', 'Jeferson', 'Giorgi', 'Maju', 'Karolyns']

# Accessing directly:
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])
print(friend_names[3])
print(friend_names[4])

print('---------------------------------------------------')

# Accessing through a for (to make it easier)
for name in friend_names:
    print(name)

print('---------------------------------------------------')

# 3.2 Accessing my friend names in a cute message
message = "Hello my dear {}, I hope you are doing fine!"

for name in friend_names:
    print(message.format(name))

print('---------------------------------------------------')

# 3.3 create your own list and use it in different messages
personal_objects = ['water bottle', 'notebook', 'laptop']

first_message = "Currently my {} is empty and I'm too lazy to fill it".format(personal_objects[0])
print(first_message)

second_message = "I bought a new {} for my english classes".format(personal_objects[1])
print(second_message)

last_message = "Even tho I have a computer, I prefer to study on my {}".format(personal_objects[-1])
print(last_message)