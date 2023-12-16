
# import another_module
# print(another_module.variablesomewhere)

# import turtle
# myobj = turtle.Turtle()

from turtle import Turtle, Screen
myobj = Turtle()
print(myobj)
myobj.shape("turtle")
myobj.color("gold1")
myobj.position()
myobj.forward(30)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


