first_name = input("Please enter your firstname: ")
middle_name = input("Please enter your middlename: ")
last_name = input("Please enter your lastname: ")

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}"
print(name_format.format(first=first_name, middle=middle_name,last=last_name))

