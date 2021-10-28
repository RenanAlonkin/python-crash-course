# 5.1 Conditional tests: write a series of conditional tests.
# Write a phrase that describes the result of your tests.
# Write at least 10 tests, with 5 trues and 5 falses. 

portuguese = 'Português'
spanish = 'Español'
print('Is portuguese the same thing as spanish?, I predict it False')
print(portuguese.lower == spanish.lower)

pedros_age = 18
legal_age = 18
print('Is Pedro allowed to drink? I predict it True')
print(pedros_age == legal_age)

my_favorite_color = 'orange'
marias_guess = 'blue'
print('Did Maria guessed my favorite color right? I predict it False')
print(my_favorite_color.lower == marias_guess.lower)

maria_nickname_in_russian = 'Masha'
marias_nickname = 'Masha'
print('is Masha a nickname for Maria? I predict it True')
print(maria_nickname_in_russian.lower == marias_nickname.lower)


answer_to_the_universe_and_everything = 'potato'
real_answer = 42
print('Is potato the answer to the universe and everthing? I predict it False')
print(answer_to_the_universe_and_everything == real_answer)

did_it_rain_today = False
prediction_of_rain_for_today = False
print('Did the weather prediction got it right? I predict it True')
print(did_it_rain_today == prediction_of_rain_for_today)

my_back_hurts = True
moms_answer = False
print('Do my mom knows about my back pain? I predict it False')
print(moms_answer == my_back_hurts)

my_eyes_color = "Brown"
my_hairs_color = "Brown"
print('Do I have the same color of eyes as my hair? I predict it True')
print(my_eyes_color.lower == my_hairs_color.lower)

do_i_deserve_a_raise = True
will_i_get_a_rase = False
print('Deserving a raise means that you will get one? I predict it False')
print(do_i_deserve_a_raise == will_i_get_a_rase)

does_russians_have_good_music = True
is_the_russian_alt_genre_the_best = True
print('Does russians have great music and the best alt genre out there? I predict it True')
print(does_russians_have_good_music and is_the_russian_alt_genre_the_best)
