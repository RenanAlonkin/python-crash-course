# 2.3 Personal Message
name = "Lara Dilara"
message = "Hey {}, I hope you had a great day!".format(name.title())
print(message)

# 2.4 Upper and lower case
upper_name = name.upper()
lower_name = name.lower()

print(upper_name)
print(lower_name)

# 2.5 Famous citation
citation = '"Yeah, I pretty much never sit by the pool anymore" - Marco Polo'
print(citation)

# 2.6 Famous Citation, pt. 2
citation_name = "Marco Polo"
citation_message = '"Yeah, I pretty much never sit by the pool anymore" - '
full_citation = citation_message + citation_name

print(full_citation)

# 2.7 Removing blank characters from names
raw_name = ' Claudia '
raw_text = "The complete string in this text is '{}'".format(raw_name)
print(raw_text)
clean_name = raw_name.split()[0]
clean_text = "The complete string in this text is '{}'".format(clean_name)
print(clean_text)
