my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
print("My favorite foods are:")
print(my_foods)

friend_foods.append('ice cream')
print("\nMy friend's favorite foods are:")
print(friend_foods)

# This isn't a copy, this is just pointing to the same space
# in the memory
other_foods = my_foods

other_foods.append('spagetti')
my_foods.append('caesar salad')

print("Let's see if other foods is equal to my foods:")
print(other_foods)
print(my_foods)