#MPH to MPS to conversion

print("Welcome to the MPH to MPS conversion app \n")

#get users input
mph = float(input("What is your speed in miles per hour: \n"))

#convert to mps and round to 2 decimal places
mps = mph * 0.4774
mps = round(mps,2) #this is a round function rounding mps to 2 decimal places

#Give an output message
print("Your speed in meters per second is " + str(mps) + ".\n")

