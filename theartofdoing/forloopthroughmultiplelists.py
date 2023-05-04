#The zip() Function 

names = ["Kwame","Kwasi","John","Alfred"]
numbers = [10, 55, 89, 90]

#using the range function in conjuction with the len function
for i in range(len(names)):
    print(names[i] + " : " + str(numbers[i]))

    print()

#now using the zip function 
for name,number in zip(names, numbers):
    print(name.title() + " : " + str(number))

