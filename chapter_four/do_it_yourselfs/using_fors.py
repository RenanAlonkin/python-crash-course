# 4.3 Couting to 20
up_to_20 = [value for value in range(1,21)]
print(up_to_20)

# 4.4 Up to a million
up_to_million = [value for value in range(1,100)]
print(up_to_million)

# 4.5 Summing the million list
min_value = min(up_to_million)
print(min_value)
max_value = max(up_to_million)
print(max_value)
sum_of_million = sum(up_to_million)
print(sum_of_million)

# 4.6 Odd numbers
odd_numbers = [odd_number for odd_number in range(1,20,2)]
print(odd_numbers)

# 4.7 Multiple of 3
multiple_of_3 = [value*3 for value in range(1,11)]
print(multiple_of_3)

# 4.8, 4.9 Cubes
cubes = [cube**3 for cube in range(1,11)]
print(cubes)