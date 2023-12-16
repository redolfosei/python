#two forms of loop
#while loop
#for loop

#for loop
#use for repeating a specific number of times

#while 
#use when you don't know how many times a loop will run for

#range function
#gives the ability to display a sequence of numbers
#range(start, stop, step) the start to stop minus 1

#print(list(range(1,8)))

#in is a membership, sequence to loop over, then colon
#for var in sequence:
    # block of code
    
# for number in range(1,11):
#     print(number)
    
#Note that, you can not use range in Strings eg for a in range(a,z)

# for i in range(1,6):
#     if i == 2:
#         print("This is " + str(i))
#     print(i)

# for i in range(0,11+1,1):
#     print(i)
    
# for i in range(10,1,-1):
#     print(i)
    
# start_number = int(input("Enter a start number here: "))
# stop_number = int(input("Enter your stop number here: "))  
# for number in range(start_number, stop_number, -1):
#     print(number)
    
#while loop
#assuming we don't know the len of this function
#while condition:
    # do something here
    
string = "coding without borders"
# count = 0
# while count < len(string):
#     count += count
# print("The len of the string is: " + str(count))

# total = 0
# for _ in range(0,len(string)):
#     print(_)
#     total += 1
    
# value = 0
# while value < 6:
#     print(value)
#     value = value + 1
# else:
#     print(value, "is not less than 6")
    
# number = 0
# count = 0
# total = 0

# while number >= 0:
#     number = int(input("Enter any number or -1 to exit the program:"))
#     if number >= 0:
#         count = count + 1
#         total = total + number
        
# average = total / count
# print("The averate is: " + str(average))

# break, continue, pass keywords in python
# break terminates the program early before the next block of code finishes;

# value = 0
# while value < 6:
#     print(value)
#     if value == 3:
#         break
#     value = value + 1 

# value = 0
# while value < 6:
#     value = value + 1 
#     if value == 3:
#         continue
#     print(value)
    
# value = 0
# while value < 6:
#     value += 1
#     if value == 3:
#         break
#     print(value)

# secret_word = 'python'
# count = 0

# while True:
#     word = input("Enter the secret word:")
#     count += 1
    
#     if word == secret_word:
#         print("Hurray!! your word matches the secret word") 
#         break 
    
#     if word != secret_word and count > 4:
#         print("You didn't guess right in " + count + "attempts")
        
         
        
    
    