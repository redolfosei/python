'''
input_string = "This is a sentence text"

def reverse_string(string):
    print(string[::-1])
    # ::-1 is a string manipulation to reverse a string

reverse_string(input_string)

input_string2 = input("Enter any string here and i will reverse it: ")
reverse_string(input_string2)
  '''        

def even_odd(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

number = int(input("Enter your number i will tell even or odd: "))
even_odd(number)
