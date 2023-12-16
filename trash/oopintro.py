# oop
# what is object oriented programming?
# self a unique identify
# Play Cry Sleep
# A person filling a form is an instance of the class;
# The form becomes the class which is the blue print;
# The person fill it with the details based on the info provided;
# On the form, we have deposit, update my records,withdraw, check balance;
# When it's in a class it's a method, when it's stand alone, it a function.
# Class(): or Class:
# Object is an instance of a class


class Baby(object):
    def __init__(self,name,gender,age):
        """ Initialising attributes """
        self.name = name.title()
        self.gender = gender
        self.age = age

        self.tired = True

    def play(self):
        if self.gender == "male":
            print(self.name + " is playing with toy cars")
        else:
            print(self.name + " is playing with toy cooking utensils")

    def cry(self):
        print("mmaaama yeeee!!!")
        print("A " + str(self.age) + " year old baby is crying!!!")

    def sleep(self):
        if self.tired == True:
            print(self.name + " is tired and sleeping...")
            self.tired = False
        else:
            print(self.name + " is not tired and NOT SLEEPIn")


confidence = Baby("Confidence W.","male",98)
mary_baby = Baby("Mary","male",7)

mary_baby.cry()




