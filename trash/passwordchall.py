import string

# def checker():
#     var_lower_cases = string.ascii_lowercase
#     var_upper_cases = string.ascii_uppercase
#     numbers = "0123456789"
#     correct_password = "Password123"
#     user_password = input("Enter the correct password here: ") 
#     if var_lower_cases in user_password and var_upper_cases in user_password and numbers in user_password:
#         print("Let's go to the next function")

def password():
    correct_password = "Password123"
    c = 0
    while True:
        
        # global c = 0
        user_password = input("Enter the correct password here: ")
        c += 1
        if user_password == correct_password:
            print("You are logged in to the system")
            break
        if user_password != correct_password and c > 4:
            print("Your " + str(c) + " attempts are exhausted, you are kicked out!!")
            break            

#checker()
password()

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# var_lower_cases = string.ascii_lowercase
# print(var_lower_cases)

# if len(user_password) >= 6 and var_lower_cases in user_password and var_upper_cases in user_password and user_password == correct_password:
#                 print("You are logged in to the system")
#                 c += 1
#         if c > 5:
#             break


# Write a program that asks the user to enter a password. 
# If the user enters the right password,the program should 
# tell them they are logged in to the system. 
# Otherwise, the program should ask them to reenter the password.
# The user should only get five tries to enter the password, after which point 
# the program should tell them that they are kicked off of the system.

# HINTS
# Take the user's input dynamically by asking them to enter it.
# You can write two functions: one that handles the password checking and one that checks 
# if the password is correct and displays the message accordingly.

# RULES FOR THE PASSWORD
# The password must be at least 6 characters long.
# The password must contain at least one uppercase letter (A–Z).
# The password must contain at least one lowercase letter (a–z).
# The password must contain at least one digit (0–9).