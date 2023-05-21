# Question 3
# Write a Python class named Circle constructed from a radius and two methods that will compute the area
# and the perimeter of a circle.

class Circle:
    def __init__(self, PIE , radius):
        self.PIE = PIE
        self.radius = radius ** 2

    def area(self):
        area = self.PIE * self.radius
        return area

    def parimeter(self):
        parimeter = 2 * (self.PIE * self.radius)
        return parimeter

circle_1 = Circle(3.14,5)
print(circle_1.area())

parimeter_1 = Circle(3.14, 9)
print(parimeter_1.parimeter())

#How can we set a constant for pie to be called in the Circle instead of entering 3.14
#Is it possible to call the area from the area function and multiply with the number 2