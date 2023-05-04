#Strings

full_name = "\tRedolf\nOsei"
#\t tabs our character
#\n moves to the next line
print(full_name)

first_name = "Redolf"
last_name = "Osei"
full_name = first_name + " " + last_name
full_name = full_name.title()
print(full_name)
print(first_name + " " + last_name)

print(5 + 3)

print ("5" + "3")

message = "find out how many H are in here, however, I want to know how you doing"

message_count = message.count("h") #very case sensitive

print(message_count)

#note that your message_count is an int and you can't concate it together with a string
#The str is a string function to turn int into string...
print("You have  " +  str(message_count) + " h's in there")
