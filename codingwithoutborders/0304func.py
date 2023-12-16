#function has it own inbuilt functions
#eg. print(), float(), max(), etc 

#devs can also build their own function. 
#function can accept a parameter
# parameter - a variable in a function 
# argument -  a value in a function.
# What if there is a variable assigned to a value in a function, is there a name for it?
# Are there maximum limit for a function parameter?

""" Function doc string """
''' Function doc string '''
#print(help(print))

# def convert(temperature):
#     fahrenheit = (temperature * 9/5) + 32
#     return f"The temperatuter {temperature} (C) is {fahrenheit}"

# print(convert(30))

# b = 5 #global var 
# def add(a,b):
#     print(a) #local var 
#     global c #global var 
#     print(b)

# def change_case(string):
#     return string.swapcase()

# change_case("PYthon")

def change_case2(string):
    output = ""
    for char in string:
        if char.islower():
            output = output + char.upper()
        if char.isupper():
            output = output + char.lower()
    return output

print(change_case2("PYthon"))
         