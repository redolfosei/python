#The input function

first_name = input("Enter your first name here: ")
first_name = first_name.title()
print("Hello " + first_name)

fav_num = input("Enter a number: ")
fav_num = int(fav_num) + 3  #fav_num on line 7 is regarded as string, so it is converted on line 8 here to int.
print("Your favourate numeber is " + str(fav_num))

print("Give me any two numbers and I will add them for you.")
num_one = input("Enter your first number: ")
num_two = input("Enter your second number: ")

'''
Another way of doing what is on line 20 is doing the below on line 12 and 13
num_one = int(input("Enter your first number: "))
num_two = int(input("Enter your second number: "))
'''
sum_nums = int(num_one) + int(num_two)

print("The sum of " + str(num_one) + " and " + str(num_two) + " is " + str(sum_nums))

print("Give me two numbers and I will multiply them ")
num_1 = float(input("Enter your first number here: "))
num_2= float(input("Enter your second number here: "))

sum_two = num_1 * num_2
print(str(num_1) + " mulitiplied by " + str(num_2) + " is " + str(sum_two))
