# Sorting elements
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

print("--------------------")

# Sorting in reverse
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

print("---------------------")

# Sorting elements but keeping the original form
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:\n{}".format(cars))

print("\nHere is the original list:\n{}".format(sorted(cars)))

print("\nHere is the original list:\n{}".format(cars))

print("---------------------")

# Showing a list in the reverse order
print(cars)

# Reverses the order of a list
cars.reverse()
print(cars)

print("---------------------")

# Discovering a list length
cars = ["bmw", "audi", "toyota", "subaru"]
length = len(cars)

print("---------------------")
