# Question 2
# Write a Python class named Rectangle constructed from length and width and a method that will compute
# the area of a rectangle. ----------------
class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        area = self.width * self.height
        return area

rectangle_1 = Rectangle(7,9)
print(rectangle_1.area())

