# Modifying an element of the list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

print("----------------------------")

# Concating an element
motorcycles.append("ducati")
print(motorcycles)

print("----------------------------")
# Creating an empty list and append it
motorcycles = []

motorcycles.append("honda")
motorcycles.append("kawasaki")
motorcycles.append("royal enfield")

print(motorcycles)
print("----------------------------")

# Adding an element
motorcycles.insert(0, "ducati")
print(motorcycles)
print("----------------------------")


# Removing elements using `del`
# If the position is known, you can use `del` to remove it
# Once the element is removed, it becomes inaccessible

del motorcycles[0]
print(motorcycles)
print("----------------------------")

# Removing elements using `pop`
# `pop` is used in stacks, to remove the last element of a list
# We can store the element that was removed
motorcycles = ["honda", "yamaha", "suzuki"]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("popped element: {}".format(popped_motorcycle))
print("----------------------------")

# Removing elements from any position on the list
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was {}.".format(first_owned.title()))
print("----------------------------")

# Removing elements based on the value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)
print("----------------------------")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print("{} is too expensive for me!".format(too_expensive))

print("----------------------------")

# The method remove will only remove the first instance of it

motorcycles = ["honda", "yamaha", "yamaha", "ducati"]
print(motorcycles)

motorcycles.remove("yamaha")
print(motorcycles)
