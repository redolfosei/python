#Adding and changing list elements

colors = ["red","green","orange"]

print(colors)
print("This is the origianl color " + colors[1])

#change green to yellow
colors[1] = "Yellow"
print(colors)
print("This is the modified color "+ colors[1])

#.append() allows to add element to a list or arrays

#Add color black to the colors
colors.append("Black")
print(colors)

#create a an empty list for colors and build them
colors_new = []
colors_new.append("White")
colors_new.append("Brown")
colors_new.append("Blue")

print(colors_new)


#.insert() method add elements at a specified index
print(colors_new[1])
colors_new.insert(1,"Pink")
print(colors_new[1])
print(colors_new)
