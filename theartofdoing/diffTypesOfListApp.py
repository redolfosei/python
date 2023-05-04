#defining list of variables 
num_strings = ["15","100","55","42"]
num_int = [15,100,55,42]
num_float = [10.2,56.0,89.5,1.7]
num_lists = [[1,2,3],[4,5,6],[7,8,9]]

print("\n\t\t\t Summary Table\n\n")

print("The variable num_strings is a: " + str(type(num_strings)) + ".")
print("It contains the elements " + str(num_strings))
print("The first element is: " + num_strings[0] + " and it is a " + str(type(num_strings[0])) + "\n")

print("The variable int is a: " + str(type(num_int)) + ".")
print("It contains the elements " + str(num_int))
print("The first element is: " + str(num_int[0]) + " and it is a " + str(type(num_int[0])) + "\n")

print("The variable num_float is a: " + str(type(num_float)) + ".")
print("It contains the elements " + str(num_float))
print("The first element is: " + str(num_float[0]) + " and it is a " + str(type(num_float[0])) + "\n")

print("The variable num_list is a: " + str(type(num_lists)) + ".")
print("It contains the elements " + str(num_lists))
print("The first element is: " + str(num_lists[0]) + " and it is a " + str(type(num_lists[0])) + "\n")

print("Now sorting num_strings and num_ints...\n")

#sort num_strings and num_ints
num_strings.sort()
num_int.sort()

#display sorted results to the user.
print("Sorter num_strings: " + str(num_strings))
print("Sorted num_int: " + str(num_int))

print("Strings are sorted alphabetically while intergers are sorted numerically! \n")