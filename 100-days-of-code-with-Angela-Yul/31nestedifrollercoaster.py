print("---Welcome to RollerCoaster!!---")
height = int(input("What is your height in cm?: \n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age Taller person?: "))
    if age < 15:
        print("Pay only $4")
    elif age <= 18:
        print("Pay $12")
    else:
        print("Pay 10 billion!! ")
else:
    print("Sorry, you have to be a bit taller before you can ride.")