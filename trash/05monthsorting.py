days = {'January':31, 
 'February':28, 
 'March':31, 
 'April':30, 
 'May':31, 
 'June':30, 
 'July':31, 
 'August':31, 
 'September':30, 'October':31, 'November':30, 'December':31}

# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
user_input = input("Enter a month here: ").capitalize()
print(f'You entered {user_input}: and there are {days[user_input]} days in {user_input}')

# (b) Print out all of the keys in alphabetical order.
sorted_keys = [key for key, _ in days.items()]
sorted_keys.sort()
print(f" Thses are the sorted months/keys {sorted_keys}")    

# (c) Print out all of the months with 31 days.
thirty_days = [key for key, _ in days.items() if _ == 31]
print(f" These are the months with 31 days {thirty_days}")

# (d) Print out the (key-value) pairs sorted by the number of days in each month
sorted_days_by_number = sorted(days.items(), key=lambda x:x[1] )
print(f" These are the months sorted by number key:value {sorted_days_by_number}")


# thirty_days_1 = [key for key, _ in days.items() if days[key] == 30]
# print(thirty_days_1)
# thirty_days_2 = [key for key, _ in days.items() if days[key] == 30]
# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])


 
    