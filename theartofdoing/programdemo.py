#counting letter APP.

#Algorithm 
#Welcome the user to the program
#take the user's name
#hello the user by name with exclamation mark
#tell the user what you will do.
#Take the users message
#take the letter he wants counted in caps 
#mention user's name and tell him the number of h's in the message both caps and lowers.

print("Hi, welcome to the APP counting machine! ")
exclamation = "!"
user_name = input("Enter your name here: ")
print ("Hello " + user_name.title().strip() + exclamation + " I will tell you the number of a letter in a message")
message = input("Enter your message here: ")
l = input("Enter the letter you want me to count ")

message = message.lower()
l = l.lower()

fm = message.count(l)
print("The number of " + l + "'s in your message is " + str(fm))


