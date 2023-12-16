# Enter a nickanme and if it includes any of these / . @ not allowed

not_include = (".","/","@")

while True:
    user_input = input("Enter a nickname here . / ; not allowed: ")
    counter_var = 0
    for char in not_include:
        if char in user_input:
            counter_var += 1

    if counter_var > 0:
        print("You entered a an invalid numebr!!!... Warning! . / ; not allowed")
    else:
        print("Hurray right name!! ")
        break



