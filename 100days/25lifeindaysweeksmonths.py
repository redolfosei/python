# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left.
# if we live until 90 years old. It will take your current age as the input and output a message
# with our time left in this format:
#     You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
expected_years = 90
expected_days = 32850
expected_weeks = 4680
expected_months = 1080

age = int(age)

converted_age_to_days = age * 365
converted_age_to_weeks = age * 52
converted_age_to_month = age * 12

days_left = expected_days - converted_age_to_days
weeks_left = expected_weeks - converted_age_to_weeks
months_left = expected_months - converted_age_to_month

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


#Another way to go about this
#These converts the remaining days straight away.
# years_remaining = 90 - age
# days_remaining = years_remaining * 356
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12