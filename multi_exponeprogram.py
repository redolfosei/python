# Multiplication and exponentiation table...

print("\n Welcome to the Multiplication and exponentiation table program...")

#get user imputs
user_name = input("\n Hey what is your name: ").title().strip()
number = float(input("What number should we start with? "))
msg = user_name + ", Maths is cool! "

#Multiplication table
print("\n Multiplication table for " + str(number) + " is.....: \n")
print("\n \t 1.0 * " + str(number) + " is " + str(round(1 * number, 4)))
print("\n \t 2.0 * " + str(number) + " is " + str(round(2 * number, 4)))
print("\n \t 3.0 * " + str(number) + " is " + str(round(3 * number, 4)))
print("\n \t 4.0 * " + str(number) + " is " + str(round(4 * number, 4)))
print("\n \t 5.0 * " + str(number) + " is " + str(round(5 * number, 4)))
print("\n \t 6.0 * " + str(number) + " is " + str(round(6 * number, 4)))
print("\n \t 7.0 * " + str(number) + " is " + str(round(7 * number, 4)))
print("\n \t 8.0 * " + str(number) + " is " + str(round(8 * number, 4)))
print("\n \t 9.0 * " + str(number) + " is " + str(round(9 * number, 4)))

#exponentiation table 
print("\n Exponentiation table for " + str(number) + " is......\n")
print("\n \t" + str(number) + " ** 1 is " + str(round(number,4)))
print("\n \t" + str(number) + " ** 2 is " + str(round(number ** 2,4)))
print("\n \t" + str(number) + " ** 3 is " + str(round(number ** 3,4)))
print("\n \t" + str(number) + " ** 4 is " + str(round(number ** 4,4)))
print("\n \t" + str(number) + " ** 5 is " + str(round(number ** 5,4)))
print("\n \t" + str(number) + " ** 6 is " + str(round(number ** 6,4)))
print("\n \t" + str(number) + " ** 7 is " + str(round(number ** 7,4)))
print("\n \t" + str(number) + " ** 8 is " + str(round(number ** 8,4)))
print("\n \t" + str(number) + " ** 9 is " + str(round(number ** 9,4)))

print("\n" + msg)
print("\t" + msg.lower())
print("\t\t" + msg.title())
print("\t\t\t" + msg.upper())

