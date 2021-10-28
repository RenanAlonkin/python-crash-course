# 4.13 Buffet: a buffet restaurant only offers 5 basic
# types of food. Think about 5 simple dishes and store
# them in a tuple.

buffet_menu = ('Lasagna', 'Carreteiro', 'Spaghetti', 'Pizza', 'Salad')

print('Welcome to our restaurant!')
print('--------------------------')
print('Buffet Menu:\n')

# Use a for loop
for dish in buffet_menu:
    print('{}'.format(dish))

# Try to change a value to see if it throws an error
try:
    buffet_menu[0] = 'Bolo de Rolo'
except Exception as e:
    print('\n', e, '\n')

# The restaurant changes it's menu

buffet_menu = ('Cordeiro', 'Parrilla', 'Sapecada de Pinhão', 'Risoto', 'Polenta frita')

print('Under new management!')

print('Welcome to our restaurant!')
print('--------------------------')
print('Buffet Menu:\n')

# Use a for loop
for dish in buffet_menu:
    print('{}'.format(dish))

