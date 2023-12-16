class Simplest:
    pass

sim = Simplest()
print(sim)
print(dir(sim))
print(type(sim) is Simplest)
print(type(sim))

#claas var and instance var
#Class var - defining a var in a class not in a fucntion
class Redolf:
    species = "Human"
print(Redolf.species)
Redolf.alive = True #class variable
print(Redolf.alive)

person = Redolf() #This is instanciation of a class
print(person.alive)

#decorator
@staticmethod
def display():
    return "This is a static fuunction"

@staticmethod
def display(s):
    return s.upper()







