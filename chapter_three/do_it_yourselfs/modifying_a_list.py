# 3.4 Guest list 
guests = ['Andrey Aguiar', 'Fernando', 'Karolyns']

message = "I would invite {} and {} to {}'s house, " \
    "because they would freakout with his hamburgers" \
        .format(guests[0], guests[2], guests[1])

invitation_message = "Hello {}, {}, {}, you are all invited "\
    "to eat some burgers hahahah."

print(message)
print('-----------------------')

print(invitation_message.format(guests[0], guests[1], guests[2]))
print('-----------------------')

# 3.5 Modifying the guest list
cant_go = 'Karolyns'
new_person = 'Lucas'
print("{} unfortunitely can't go :/, but I'm going to invite {}".format(cant_go, new_person))
guests[2] = new_person

print(invitation_message.format(guests[0], guests[1], guests[2]))
print('-----------------------')

# 3.6 New guests
# Inserting in the first position
guests.insert(0, 'Amanda')
# Inserting in the middle
guests.insert(3, 'Jeferson')
# Appending to the end of the list
guests.append('Gabes')

invitation_message = 'Hello {}, you are invited to my house to eat some burgers'

for guest in guests:
    print(invitation_message.format(guest))

print('-----------------------')

# 3.7 Reducing the list of guests
excuse_message = "Unfortunitely we can't have that many people, corona, you know...."
print(excuse_message)

while len(guests) > 2:
    uninvited_guest = guests.pop()
    print("Hey {}, unfortunitely I will need to reschedule!".format(uninvited_guest))

print('Lets check who are still here in the list...')
for guest in guests:
    print(invitation_message.format(guest))

print("It isn't fair with the rest of the folks, I'm going to cancel")
del guests[0]
del guests[0]

print(guests)