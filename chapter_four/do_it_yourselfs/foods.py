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
my_foods.append('temaki')

print("Let's see if other foods is equal to my foods:")
print(other_foods)
print(my_foods)

# 4.10 Show the first 3 items
print('The first 3 items on the list are:')
print(my_foods[:3])
# 4.10 Show the 3 items in the middle

# Let's create a method that gives us the list middle element
def middle_element(lst):
    if len(lst) % 2 != 0:
        return len(lst) // 2
    else:
        return len(lst) // 2 - 1

middle_index = middle_element(my_foods)
print('The 3 middle ones are:')
print(my_foods[middle_index-1:middle_index+2])

# 4.10 Show the last 3 items
print('The last 3 items on the list are:')
print(my_foods[-3:])

# 4.11 Pizzas
# Add a new pizza to the original list
my_pizzas = ['brocolis with catupiri', 'dried tomato', '4 cheeses']
my_pizzas.append('peperoni')
friend_pizzas = my_pizzas[:]

print('My pizzas:', my_pizzas)
print('Friend pizzas:', friend_pizzas)

# 4.12 Using loops
message = "I like {} pizza.\n"
for pizza in my_pizzas: 
    # Use the phrase I like 
    print(message.format(pizza.title()))

message = "My friend likes {} pizza.\n"
for pizza in friend_pizzas: 
    # Use the phrase my friends like
    print(message.format(pizza.title()))

