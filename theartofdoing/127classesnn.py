# Creating a Class

# Class ---> Blueprint to build something
# Object ---> Waht you build
# Instance ---> What you work with once it is built
# Attribute ---> Information used to distinguish one instance  from another in a class
# Method ---> Behaviour common to all instances of a class (function)

class Baby():
    """ A simple class to simulate a baby """
    """ The self is a way for an object to identify itself """
    def __init__(self, name, gender, age):
        """ Initialize attributes """
        self.name = name.title()
        self.age = age

        self.tired = True

    def play(self):
        pass

    def cry(self):
        pass

    def sleep(self):
        pass

little_boy = Baby("Kofi", "male", 3)
little_girl = Baby("Mary", "female", 5)

print(little_boy.name)