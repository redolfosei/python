#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator.\n")
bill = float(input("What was the total bill ?: \n"))
user_percentage = float(input("What percentage tip would you like to give? 10,12 or 15?: \n"))
number_of_people = int(input("How many people to split the bill?: "))

tip_percentage = user_percentage / 100
tippercent_and_totalamount = tip_percentage * bill
total_bill = bill + tippercent_and_totalamount
each_pays = total_bill / number_of_people

#print(f"This is percentage: {tippercent_and_totalamount}")
print(f"Each person should pay: {round(each_pays,2)}")