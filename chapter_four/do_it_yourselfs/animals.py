# 4.1 - write down some animals
animals = ["rat", "parrot", "ferret"]

message = "{} would be a great pet!"
for animal in animals:
    # Use the phrase "would be a great pet!"
    print(message.format(animal.title()))

# Write a message after the for
print("Any of those animals would be a great pet!")
