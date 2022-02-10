# 7.4 Pizza Ingridients

pizza_ingridients = []
active = True
first_execution = True

print("Welcome to our pizza shop. I'm Renan and I'm going to be your host tonight.")
print("To add ingridients, you just need to write them down into the prompt!")
print("Whenever you want to leave, just write quit and we will prepare your pizza.")

while active:
    if(first_execution):
        ingridient = input("Tell me, what ingridient should we add to your pizza?\n")
        first_execution = False
    else:
        ingridient = input("Hmm, something else?\n") 
    
    if ingridient == "quit":
        break
    
    pizza_ingridients.append(ingridient)

print("-----------------------------------------")
print("Your order is:")
print(*pizza_ingridients, sep = ", ")

