#The type function

name = "RedolF Osei"
fav_num = 23
tax_rate = 10.90

print(type(name))
print(type(fav_num))
print(type(tax_rate))
print()
#Casting is the term that is used to change a variable type

tax_rate = str(tax_rate)
print(tax_rate)
print(type(tax_rate))
print()

print(name.title() + "'s favourate number is " + str(fav_num) + ".")

print()
print(name.title(),"'s favourte number is ", fav_num, ".")
