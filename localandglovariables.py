'''
number1 = 900 #this is a global variable and ca be used anywhere

def fun1():
    number2 = 20 #this is a local variable and cannot be used outside the func
    print(number2)

fun1()


print(number1) #this is a global variable and ca be used anywhere
'''

#you can use global in func by specifying global

def fun1():
    global number2 #this is now a global number
    number2 = 20

fun1()
print(number2)
