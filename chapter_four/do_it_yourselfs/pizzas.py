# 4.1 - write down the pizzas you like:
pizzas = ['brocolis with catupiri', 'dried tomato', '4 cheeses']

message = "I like {} pizza.\n"
for pizza in pizzas: 
    # Use the phrase I like 
    print(message.format(pizza.title()))

# Write a message after the for talking about how you like pizza
print("Writing this down I realized that meat is not necessary in a pizza")
print("For example, I like {} because I like brocolis, I always did".format(pizzas[0]))
print("I also like {} because I love green.".format(pizzas[1]))
print("And for last but not least, {} because I simply love cheese.".format(pizzas[2]))