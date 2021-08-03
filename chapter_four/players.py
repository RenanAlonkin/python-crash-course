players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Will print the first 3
print(players[0:3])

# Will print the last 3
print(players[1:4])

# Will print from the 1st one to the 3rd
print(players[:4])

# Will print the 3rd to the last one
print(players[2:])

# Will print the last 3 elements
print(players[-2:])

# Running through a slice with a loop
print("Here are the first three players of my team:")
for player in players[:3]:
    print(player.title())

