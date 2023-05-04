#tuple is an immutable list. We use this when you do not want to change the scope of your program

grades = [100,59,39,89]
grades_tupl = (88,99,45)

print(grades)
print(grades_tupl)

print(type(grades))
print(type(grades_tupl))

grades.append(72)
print(grades)

#tuples are immutable so if you try to add, append or pop, you get an err msg
#with tuples, you can overide. 

grades_tupl = (12,39,89)
print(grades_tupl)
