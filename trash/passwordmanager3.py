# Coding Challenge main solution 

def password_check(password):
    lower_case = False
    upper_case = False
    number = False
    if len(password) >= 6:
        for char in password:
            if char.islower():
                lower_case = True
            if char.isupper():
                upper_case = True
            if char in "0123456789":
                number = True
    else:
        print("password length should be more than 6")

    if lower_case and upper_case and number:
        return True
    else:
        return False


def password1():
    max_num_attempts=5
    count=0
    while count < max_num_attempts:
        password=input("Enter a password:") 
        print(count)
        if (password=="Password123") and password_check(password):
            print("You are logged in the system :")
            break 
        else:

            print("Re-enter your password: ")
            
        count+=1
        
    if max_num_attempts==count:
        print(count)
        print("You are kicked of the system ")

password1()
