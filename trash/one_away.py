# Write a function called one_away that takes two strings and returns True if the strings are of the same length 
# and differ in exactly one letter, like bike/hike or water/wafer.

def differ(f_string,s_string):
    c = 0
    match = False
    if len(f_string) == len(s_string):
        for i in range(len(f_string)):
            for j in s_string:
                if f_string[i] != s_string[j]:
                    match = True
                    break
                else:
                    match = False
    else:
        print("Lenght are not same")
    

