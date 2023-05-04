n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n)) #print in base 10... d stands decimal number
print("my number is {:b}".format(n)) #print in base 2 or binary

print("{:f}".format(f)) #prints a floating point number
print("{:.3f}".format(f)) #print the first three digits of f
print("{:11.3f}".format(f)) #padded additional 11 characters and this pad with spaces
print("{:011.3f}".format(f)) # however you can pad with a number like 0
print("{0} {1} {2}".format(n,f,s)) #printing all variables above

print("{name} owns {amount} of {object}'s ".format(
name = "redolf",
amount = 7,
object = "apples"
))



#There are many other types such as:
# e - exponents
# b - binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadecimal (base 16)
# f - Floats (decimal numbers)
# s - strings (default if none is specified)

