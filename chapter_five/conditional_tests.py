# 5.2 More conditional tests
# Write down at least one True and one False for the 
# following cases:

# Equals and Not Equals with strings
piauis_podcast_name = 'Foro de Teresina'
guessed_name = 'Podcast da Piaui'
print('Is guessed name equal to the real name?', guessed_name == piauis_podcast_name)

current_role = 'Programmer'
type_of_professional_we_are_looking_for = 'Data Scientist'

if(current_role != type_of_professional_we_are_looking_for):
    print("Sorry, unfortunetly you don't fill one of the requirements for this role.")
else:
    print("Congratulations, you've been accepted in our hiring process!")

# Create a test using the function lower()
username = 'RenanSteinck'
inputted_username = "ReNaNSTeiNcK"

if(username.lower() == inputted_username.lower()):
    print('Username already exists')
else:
    print('Account created successfuly')


# Numeric tests (greater, greater or equal to, etc)
legal_age_to_drink_alcohol = 18
acceptable_age_for_buying_alcohol = 17 # This is just a made up number lol
actual_age = 20

if(actual_age >= legal_age_to_drink_alcohol):
    print('Here, take a beer!')
elif (acceptable_age_for_buying_alcohol == actual_age):
    print("Show me your parent's letter young boy!")
else:
    print("Sorry, you don't have enough age to buy alcohol.")

# Numeric tests and conditionals (and and or)
male_retirement_age = 65
female_retirement_age = 60
sex = "M"
actual_age = 32

if(sex == "M" and actual_age <= male_retirement_age):
    print("It will take you", male_retirement_age - actual_age, " years to retire")
elif(sex == "F" and actual_age <= female_retirement_age):
    print("It will take you", female_retirement_age - actual_age, "years to retire")

# Is in the list
vip_list = ['Charles', 'Boyle', 'Fernando', 'Gregory']
your_name = 'Yosef'

if(your_name in vip_list):
    print('Okay, he is cool, let him in!')
else:
    print('Sorry bro, your name is not on the list.')

# Is not in the list

im_alergic_to = 'Cinnamon'
ingredients = ['Banana', 'Blue Berry', 'Sugar', 'Strawberry']

if(im_alergic_to not in ingredients):
    print("All good, you can eat.")
else:
    print("DON'T EAT THAT!!!!!!!!")