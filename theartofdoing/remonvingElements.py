# removing elements from list

colors = ["Red","Yellow","Green","Black","Blue"]

#.romove() takes one argument, the element you wish to remove
#if you try to reference an element which does not exist, you get an err msg
print(colors)
colors.remove("Yellow")
print(colors)

# how to assing a new var to an old var new_var = colors 
#the romove method will remove once as if there are duplicates, eg,
new_colors = ["White","Purple","Orange","White","Green"]
new_colors.remove("White")
print(new_colors)
print()
#there are two White in this list, but only the first one is removed
#now if I remove again, sure enough, it will remove the next index 
new_colors.remove("White")
print(new_colors)
#note, the .remove() method removes element completely, gone forever 
print()

#.pop() method allows us to remove element but returns the element.
#.pop() method takes index argument, eg colors.pop(1)
#.pop() method used without an arguement, pops off the last element in a list
new_colors2 = ["Black","Purple","Orange","White","Green"] 
print(new_colors2)
new_colors2.pop()
print(new_colors2)

print()
#now we can store a removed element in a variable, eg we can use the default pop method to remove the last element

new_colors3 = ["Pink","Purple","Orange","White","Gray"]
print(new_colors3)
grayRemoved = new_colors3.pop()
print("This is the color removed " + grayRemoved)
print ()

new_colors4 = ["Brown","Green","Purple","Orange","White","Gray"]
print(new_colors4)
bd_color = new_colors4.pop(1)
print("The bad color is " + bd_color)
print()
#del 
print(new_colors4)
del new_colors4[0]
print(new_colors4)

cars = []
cars.append(input("Enter a car here: "))
cars.append(input("Enter a car here: "))
cars.append(input("Enter a car here: "))

print(cars)
