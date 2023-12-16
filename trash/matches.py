# Write a function called matches that takes two strings as arguments and returns how many matches there are between the strings. 
# A match is where the two strings have the same character at the same index. For instance, 
# 'python' and 'path' match in the first, third, and fourth characters, so the function should return 3.

def matches(first_string,second_string):
    c = 0
    d = 0
    e = 0
    for i in range(len(second_string)):
        if first_string[0] == second_string[0]:
            c += 1
        if first_string[1] == second_string[1]:
            d += 1
        if first_string[2] == second_string[2]:
            e += 1   
            
    return f" {c + d + e} matches were found!  "  
                             
print(matches("python","path"))






















# def matches(first_string,second_string):
#     for char in first_string:
#         if second_string[0] in char[0]:
#             print(char)