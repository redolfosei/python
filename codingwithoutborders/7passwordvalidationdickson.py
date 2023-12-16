def isValid(string: str) -> bool:
    contains = "!@#$%^&*"
    # Keeping track of the number, symbol, lowerCase, and upperCase characters
    number, str_low, str_high,symbol = 0,0,0,0 # 0011  1111
    # if the length of string is not 8 or more
    # This condition will not be checked
    if len(string) >= 8:
        # Checking for all the initialized variables
        for ch in string:
            if (ch.islower()):
                str_low += 1
            if (ch.isupper()):
                str_high += 1
            if ch.isdigit():
                number += 1
            if ch in contains:
                symbol += 1
    # if the initialized variable is not at least == 1 or more
    if (number >= 1 and symbol >= 1 and str_low >= 1 and str_high >= 1) and (number + symbol + str_low + str_high == len(string)):
        return True
    else:
        return False

print(isValid("Hello!123@"))
print(isValid("Hello"))
print(isValid("Pssw0rd"))
print(isValid("12345678"))
print(isValid("passWORD"))
print(isValid("p@ssWORD"))