# Write a program that calculates the grade for a student based on their test scores.
# The program should take three test scores as input and calculate the average.
# Then, based on the average score, assign a letter grade according to the following criteria:
#
#     Average score >= 90: A
#     Average score >= 80: B
#     Average score >= 70: C
#     Average score >= 60: D
#     Average score < 60: F
#
# Your task is to create a function called
# calculate_grade
# that takes three test scores as parameters and returns the corresponding letter grade as a string.

print("--- Welcome to the Grade Calculator APP ---")

def calculate_grade():
    first_score = float(input("Enter your first score here: "))
    second_score = float(input("Enter your second score here: "))
    third_score = float(input("Enter your second score here: "))

    total_of_three_numbers = first_score + second_score + third_score

    average_o = total_of_three_numbers  / 3

    print("Your average is {0} ".format(average_o))

    if average_o >= 90:
        print("A")
    elif average_o >= 80:
        print("B")
    elif average_o >= 70:
        print("C")
    elif average_o >= 60:
        print("D")
    elif average_o < 60: #this part can just be handled with the else block;
        print("F")

calculate_grade()
