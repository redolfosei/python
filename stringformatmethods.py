#String formating methods

name = "Redolf"
age = 45
money = 10.98

#print this using string concatenation
print(str(name) + " is " + str(age) + " years old and he is wealth $" + str(money))

#print using the format method.
print("{0} is {1} years old and he is wealth $ {2}".format(name, age, money))

#print using the f - string
print(f"{name} is {age} years old and he is wealth $ {money}")
