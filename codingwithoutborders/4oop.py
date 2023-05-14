#Classe

class Car:
    def init(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.speed=0

    def accelerate(self):
        self.speed=self.speed+10
        return f"The {self.make} is now going {self.speed} mph"

    def brake(self):
        self.speed = self.speed - 10
        return f"The {self.make} is going {self.speed} mph"

Toyota = Car("Toyota","Corolla", "2021")

print(Toyota.brake())






















# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self):
#         self.speed = self.speed+10
#         return self.speed




