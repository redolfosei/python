'''
def print_student_name():
    print('Name of Studnet')

def print_student_age():
    print('Age of student')

print_student_age()
'''

import random

def getNumber(number):
    if number == 1:
        return 'The randmom number selected is 1'
    elif number == 2:
        return 'The randmom number selected is 2'
    elif number == 3:
        return 'The randmom number selected is 3'
    elif number == 4:
        return 'The randmom number selected is 4'
    elif number == 5:
        return 'The randmom number selected is 5'

random_number = random.randint(1,5)
pick = getNumber(random_number)
print(pick)

    
