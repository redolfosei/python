import random
class Baby():
    """ A simple class to simulate a baby """
    """ The self is a way for an object to identify itself """
    def __init__(self, name, gender, age):
        """ Initialize attributes """
        self.name = name.title()
        self.age = age
        self.gender = gender

        self.tired = True

    def play(self):
        """ Simulate Play based on gender """
        if self.gender == "male":
            print(self.name + " is playing with toy cars")
        else:
            print(self.name + " is playing with toy utensils")

    def cry(self):
        """ crying """
        print("maama yehhhh yeeeeeeeee!")
        print("A " + str(self.age) + " year old is crying")

    def sleep(self):
        """ Sleeping """
        if self.tired == True:
            print(self.name + " is sleeping")
            self.tired = False
        else:
            print("The baby " + self.name + " isn't tired and not sleeping!...")

little_boy = Baby("Kofi", "male", 3)
little_girl = Baby("Mary", "female", 5)

print(little_boy.name)
print(little_boy.name + " is a " + str(little_boy.age) + " year old " + little_boy.gender + ".")

little_boy.play()
little_girl.play()

little_boy.cry()
little_girl.cry()

little_boy.sleep()
little_girl.sleep()

little_boy.sleep()

babies = []
for i in range(25):
    num = random.randint(0,1)
    if num == 0:
        gender = "male"
    else:
        gender = "female"

    age = random.randint(0,5)

    baby = Baby(str(i), gender, age)
    babies.append(baby)

for baby in babies:
    print("baby # " + baby.name + " is a " + str(baby.age) + " year old " + gender)