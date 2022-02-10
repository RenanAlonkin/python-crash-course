# 7.4 Pizza Ingridients

from soupsieve import match


total_cost = 0
amount_of_tickets = 0
active = True

less_than_3 = 0
tree_to_twenty = 10
twenty_or_more = 15

first_execution = True

print("Welcome to 'bad movies' cinema. I'm Renan and I'm going to be your host tonight.")
print("I will need to check your ids, please. We have a discount policy based on age,")
print("Write it down your age, and I'm going to tell you the price. Write down 'done' and we will")
print("conclude your purchase.")

while active:
    value = None
    if(first_execution):
        value = input("Sooo, let's check your first, what is your age?\n")
        first_execution = False
    else:
        value = input("Hmm, anything else?\n") 

    if value == "done":
        break

    if(int(value) <= 3):
        print("That is on the house!")
        total_cost += less_than_3
    elif(int(value) > 3 and int(value) <= 12):
        print("That will be 10")
        total_cost += tree_to_twenty
    elif(int(value) > 12):
        print("Hmm, that will be 15")
        total_cost += twenty_or_more


    amount_of_tickets += 1
    

print("-----------------------------------------")
print("Your order is:")

print("So, it will be {} ticket(s). The total will be {}"
    .format(amount_of_tickets, total_cost)
)