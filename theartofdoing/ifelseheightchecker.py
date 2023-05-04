print("Welcome to the rollercoaster!")

height = int(input("Enter your height here in cm: "))

if height >= 120:
    print("You are qualified to ride the rollercoaster")
    age = int(input("What is your age: "))
    if age < 12:
        print("You are a kid pay just $4")
    elif age <= 18:
        print("Pay just $7 and enjoy")
    else:
        print("You are 18 or above pay $12")
else:
    print("Sorry you need to grow taller before you ride")


