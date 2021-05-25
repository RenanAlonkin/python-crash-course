name = "ada wong"

# Makes the first letters Uppercase
print(name.title())
# Makes it all upper case
print(name.upper())
#Makes it all lower case
print(name.lower())

# Combining or concating strings
first_name = "ada"
last_name = "wong"

# Concating
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Breaking lines and tab
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tJavascript")

# Removing white spaces
favorite_language = "python "
# Operates a strip on the right
print(favorite_language.rstrip())

favorite_language = " python "
# Removing strip on both ends
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())


