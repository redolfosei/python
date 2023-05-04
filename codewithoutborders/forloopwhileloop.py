# Loops are used to run a block of code for a certain number of times. 
# It is used to iterate over any sequences such as list, tuples, string. 

# syntax for for loop
# for number in sequence:
#   print(number)


#numbers = [1,2,3,4,5,6,7,8]
#for numbers in numbers:
#    print(numbers)

# sentence = "Coding without borders"
# for word in sentence.split():
#     print(word)

program = {
    "name": "coding without borders",
    "instructors": ["Wells", "Optis","Dicks"],
    "language": "Python programming",
    "time": "3pm GMT",
    "Days": "Every Sunday"
}

instructors = program["instructors"]
for instr in instructors:
    print(instr)

# for key in program["instructors"]:
#     print(key)


