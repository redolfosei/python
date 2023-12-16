def isPasswordValid(password):
    #Length check
    if len(password) < 8:
        return False
        #print("We leave you here")

    #Uppercase check
    hasUppercase = False
    for c in password:
        if c.isupper():
            hasUppercase = True

    #Lowercase check
    hasLowercase = False
    for c in password:
        if c.islower():
            hasLowercase = True

    #Digit check
    hasDigit = False
    for c in password:
        if c.isdigit():
            hasDigit = True

    # # Special character check
    # hasSpecial = False
    # punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # for c in punctuation:
    #     if password in punctuation:
    #         hasSpecial = True

    # Validity check
    if hasUppercase and hasLowercase and hasDigit:
        return True
        #print("Valid")
    else:
        return False
        #print("false")

print(isPasswordValid("Password123!"))
print(isPasswordValid("hello"))
print(isPasswordValid("123456789"))
print(isPasswordValid("passWORD"))
print(isPasswordValid("P@ssw0rd"))































# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
# printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# #whitespace = ' \t\n\r\x0b\x0c'
#
# password = input("Enter your password here: \n")
#
# if len(password) >= 8:
#     uppercase = [item for item in ascii_uppercase if item in ascii_uppercase]
#         print(uppercase)
# else:
#     print(f"You failed the first requirement, Goodbye!")


# def isPasswordValid(password):
#     length_check = len(password) >= 8
#     uppercase_check = any(x.isupper() for x in password)
#     lowercase_check = any(x.islower() for x in password)
#     digit_check = any(x.isdigit() for x in password)
#     special_character_check = any(not x.isalnum() for x  in password)
#
#     return length_check and uppercase_check and lowercase_check and digit_check and special_character_check


