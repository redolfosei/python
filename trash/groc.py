#welcome.

# PSUDOCODE (Hands on trial)
# 1. Welcome the user to the application.
# 2. Display to the user today's date (Month/Day Hour/Minute)
# 3. Display to the user what is in the list.(Cheese and Meat)
# 4. Allow the user to add additional shopping items to the list.
# 5. Display what the user has entered together with what was already in the list.
# 6. Sort all the list in alphabetical order A-Z
# 7. Display the sorted list to the user
# 8. Allow the user to remove some of the items if he/she wants to.
# 9. Display the rest of the items.

import datetime
welcome = "Welcome to the Grocery List App!\n"
print(welcome)

dateTime = datetime.datetime.now()
month = dateTime.month
day = dateTime.day
hour = dateTime.hour
minute = dateTime.minute

shoppingList = ["Meat","Cheese"]
print("Time and date: " + str(month) + "/" + str(day) + "\t" + str(hour) + ":" + str(minute))




