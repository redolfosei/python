#Grader sorter APP

#initiliaze list and get the user's input
print("\nwelcome to the Grade sorter APP \n")

grades = []

grade = int(input("Enter your 1st grade here: (0 to 100) "))
grades.append(grade)

grade = int(input("Enter your 2nd grade here: (0 to 100) "))
grades.append(grade)

grade = int(input("Enter your 3rd grade here: 0 to 100: "))
grades.append(grade)

grade = int(input("Enter your 4th grade here: 0 to 100: "))
grades.append(grade)

#output what the user entered
print()
print("Your grades entered are: " + str(grades))

#sort grades from highest to lowest
grades.sort(reverse = True)

print()
print("Your grades from highest to lowest are "+ str(grades))

#remove the two lowest grade and output it to the user
print()
firstDropped = grades.pop(3)
secondDropped = grades.pop(2)
print("Your first grade dropped is: " + str(firstDropped))
print("Your second grade dropped is: " + str(secondDropped))

#output the grades that are remaining to the user
print()
print("Your remaining grades are: " + str(grades))

#Tell the user his highest grade now. 
print()
print("Your highest grade is: " + str(grades[0]) + ".\n")

'''Another way to do line 32 is this below, doing it twice: 
removedGrade = grades.pop()
print("Your removed grade is: " + str(removedGrade))
removedGrade = grades.pop()
print("Your removed grade is: " + str(removedGrade))
'''