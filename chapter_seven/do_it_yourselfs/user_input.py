# 7.1 Car Dealer
print("-----------------")
print("7.1 - Car Dealer")
print("-----------------")

print("Hello, welcome to our car dealer, I'm Renan.\n")

car_brand = input("How can I help you? Oh, a car? What brand do you want? ")
print("Hmmmm, let me see if I can find a {} for you".format(car_brand))

# 7.2 Restaurant
print("-----------------")
print("7.2 - Restaurant")
print("-----------------")

print("Welcome, Welcome, thanks for choosing Renan's restaurant.\n")
amount_of_people = int(input("So, how many are you? "))
if amount_of_people >= 8:
    print("Hmmmmm, I'm sorry, we only have one table that big in the house...")
    print("Do you mind waiting?")
else:
    print("Oh, great, let me find a table for you!")

# 7.3 Multiple of 10
print("-----------------")
print("7.3 - Multiple of 10")
print("-----------------")

print("Let's see, hmmmm, Let's figure it out if that number is multiple of 10.\n")
number = int(input("Enter a number: "))
if number % 10 == 0:
    print("Ohhh, interesting, that number is multiple of 10.")
else:
    print("Hmmm, that is not multiple of 10.")
