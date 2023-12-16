print("---Welcome to RollerCoaster!!---")
height = int(input("What is your height in cm?: \n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age Taller person?: "))
    if age < 12:
        print("Childs ticket Pay only $4")
    elif age <= 18:
        print("Pay $12")
    else:
        print("Adult tickets are 18!! ")
    wants_photo = input("Do you want a photo taken? Y or N. ")     
else:
    print("Sorry, you have to be a bit taller before you can ride.")
    
    