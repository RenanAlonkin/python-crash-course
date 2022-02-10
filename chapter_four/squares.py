# Print all squares until 10
squares = []

for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


# Using list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)
