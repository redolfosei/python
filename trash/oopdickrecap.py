print(type("Confidence"))
fname = "Confi"
print(type(fname))

class Sim:
    pass

sim = Sim()
print(dir(sim))
print(type(sim) is Sim) #Can you say this is checking if the instace of the class has the attributes of the Class

# class variables and instance variable;
# class variables can be accessed with the class and the instance of the class
class Sym:
    vines = "This is vines"
    age_of_vines = 29
    print(f"This is inside the class {vines}")
sim = Sym()
print(sim.vines)
print(sim.age_of_vines) #This is using the Class to access the age_of_vines directly

#instance variables
class Sym:
    def __init__(self,first_name,sur_name):
        self.first_name = first_name
        self.sur_name = sur_name

sim = Sym("Richard","Azure")
print(sim.sur_name)

# Sym = Sym("Kofi","Odoi")
# print(Sym.first_name)

class Person:
    def __init__(self,human_age,human_color):
        self.human_age = human_age
        self.human_color = human_color

    def fairordark(self):
        if self.human_color == "fair":
            print(f"{self.age} is fair")
        else:
            print(f"{self.age} is black")

person_1 = Person(67,"fair")
print(person_1.human_color)

class PersonTwo(Person):
    def fairordark(self):
        print("Complsory you are BLACK")

mary = PersonTwo(56,"yellow")
print(mary.human_age,mary.human_color)
mary.fairordark()











