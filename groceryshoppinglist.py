# import datetime
# dateTime = datetime.datetime.now()
# month = str(dateTime.month)
# day = str(dateTime.day)
# hour = str(dateTime.hour)
# minute = str(dateTime.minute) with this dateTime has been casted to str already

import datetime
dateTime = datetime.datetime.now()
month = dateTime.month
day = dateTime.day
hour = dateTime.hour
minute = dateTime.minute

shoppingList = ["Meat","Cheese"]

# welcome users, give them date and time and what they have in their list
print("\nWelcome to the Grocery List APP!")
print("current date and time: " + str(month) + "/" + str(day) + "\t" + str(hour) + ":" + str(minute))
print("You have " + str(shoppingList[0]) + " and " + str(shoppingList[1]) + " in your list now.\n")

#Take input from user, its alway good to store in a variable before appending
product1 = input("Type the food to add to the grocery list: ")
product2 = input("Type the food to add to the grocery list: ")
product3 = input("Type the food to add to the grocery list: ") 

#now you append all into the shoppingList
shoppingList.append(product1.title())
shoppingList.append(product2.title())
shoppingList.append(product3.title())

print("\nHere is your grocery list: ")
print(shoppingList)
print("Here is your grocery list sorted: ")
#sort the grocery list and display to the user. 
shoppingList.sort()
print(shoppingList)

print("\n Simulating Grocery shopping list...\n")
print("What food do you want to remove from your list")
cL = len(shoppingList)
print("Current grocery list: " + str(cL) + " items.")
print(shoppingList)
print("\nWhat food did you buy? ")


