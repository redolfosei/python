#triangle solver app

import math # This import math library for higher mathematical operations

print("Welcome to the Triangle Area calculation App: ")

first_leg = float(input("Enter the first leg of triangle here: "))
second_leg = float(input("Enter the second leg of triangle here: "))

#calculations
h = math.sqrt(first_leg**2 + second_leg**2)
h = round(h,3)

#calculation for the area
area = 0.5*first_leg * second_leg
area = round(area,3)

print("For a triangle with " + str(first_leg) + " and " + str(second_leg) + " legs, the hypotenuse is " + str(h))
print("For a triangle with " + str(first_leg) + " and " + str(second_leg) + " legs, the area is " + str(area))
