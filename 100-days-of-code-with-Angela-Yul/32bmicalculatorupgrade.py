# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
    #print("Your BMI is {0}, you are underweight.".format(bmi))
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
    #print("Your BMI is {0}, you have a normal weight.".format(bmi))
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
    #print("Your BMI is {0}, you are slightly overweight.".format(bmi))
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
#print("Your BMI is {0}, you are obese.".format(bmi))
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    #print("Your BMI is {0}, you are clinically obese.".format(bmi))






